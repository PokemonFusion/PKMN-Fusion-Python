import copy, random
import sys, os
sys.path.append(os.path.abspath(os.path.join('')))
from CombatCode.pokemonCombinedDex import BattlePokedex as dex
class Pokemon:




    # dict of all the natures and their stat bonuses
    # there's nothing preventing the addition of natures that modify hp,
    # or more than two stats, or have a different bonuses from +10% and -10%.
    # This is static.
    NATURES = {
        "Hardy":     {},
        "Lonely":    {'atk': 1.1, 'def': 0.9},
        "Brave":     {'atk': 1.1, 'spe': 0.9},
        "Adamant":   {'atk': 1.1, 'spa': 0.9},
        "Naughty":   {'atk': 1.1, 'spd': 0.9},
        "Bold":      {'def': 1.1, 'atk': 0.9},
        "Docile":    {},
        "Relaxed":   {'def': 1.1, 'spe': 0.9},
        "Impish":    {'def': 1.1, 'spa': 0.9},
        "Lax":       {'def': 1.1, 'spd': 0.9},
        "Timid":     {'spe': 1.1, 'atk': 0.9},
        "Hasty":     {'spe': 1.1, 'def': 0.9},
        "Serious":   {},
        "Jolly":     {'spe': 1.1, 'spa': 0.9},
        "Naive":     {'spe': 1.1, 'spd': 0.9},
        "Modest":    {'spa': 1.1, 'atk': 0.9},
        "Mild":      {'spa': 1.1, 'def': 0.9},
        "Quiet":     {'spa': 1.1, 'spe': 0.9},
        "Bashful":   {},
        "Rash":      {'spa': 1.1, 'spd': 0.9},
        "Calm":      {'spd': 1.1, 'atk': 0.9},
        "Gentle":    {'spd': 1.1, 'def': 0.9},
        "Sassy":     {'spd': 1.1, 'spe': 0.9},
        "Careful":   {'spd': 1.1, 'spa': 0.9},
        "Quirky":    {},
    }
    
    # Get the XP Rate of the pokemon in question.
    def getXPRate(self):
        # sdic = self.getDic()
        # base = sdic.get("baseSpecies")
        # if base is not None:
        #     sdic = self.getDic(base)
        # rate = sdic.get("growthRateId")
        rate = self.getDicEntry("growthRateId")

        ratedict = {
            1 : "slow",
            2 : "mediumfast",
            3 : "fast",
            4 : "mediumslow",
            5 : "erratic",
            6 : "fluctuating"
        }
        return ratedict.get(rate)

        


    def __init__(self, ot, species = "missingno", nickname = None, gender = None, isEgg = False, level = 1, ability = random.choice(["0","1"])):
        
        # sdic is the dictionary entry for the species.
        sdic = None
        try:
            sdic = dex[species.lower()] # Retrieve the dictionary for the species. lower() is used as a safeguard against programmer error, since uppercase keys do not exist in this dictionary (if they do, they should be corrected).
        except KeyError:
            sdic = dex["missingno"] # If the key is not found, default to missingno.
        
        # Pokemon species, as a dict key
        # this should always be set in actual Pokemon, as a lot of info is derived directly
        # from species definitions
        self.species = species
        
        # the pokemon's nickname, as a string
        # if None, then the displayed name should be the species's display name
        self.nickname = nickname
        
        # gender as a string
        # like in species definitions, should be 'M', 'F', or 'N'
        if gender != None: # If the gender is provided, just use that.
            self.gender = gender
        else: # Otherwise, choose a random valid gender.
            self.gender = sdic.get("gender") # Set gender to default value, if there is one.
            if self.gender == None: # If there isn't, randomize it.
                genderRatio = sdic.get("genderRatio") # Temporary variable to assist in determining gender.
                #if no gender ratio is found, it's 50/50
                if genderRatio == None: 
                    self.gender = random.choice(["M", "F"])
                # Randomly set gender according to ratio provided.
                elif random.random() < genderRatio["M"]:
                    self.gender = "M"
                else:
                    self.gender = "F"
        
        # nature, as a string
        self.nature = random.choice(["Hardy","Lonely","Brave","Adamant","Naughty","Bold","Docile","Relaxed","Impish","Lax","Timid","Hasty","Serious","Jolly","Naive","Modest","Mild","Quiet","Bashful","Rash","Calm","Gentle","Sassy","Careful","Quirky"])
        
        # ability, as a string
        # like in species definitions, should be '0', '1', or 'H'
        # note that species without second or hidden abilities should still be able to
        # get '1' and 'H', as evolutions will inherit this
        # a getter function below will handle translating these into actual ability keys
        self.ability = ability
        
        # ot, as a dbref
        # this could also be turned into a string of numbers like in the games,
        # but that's probably not needed and poor in the long-term
        # Note that wild encounters will automatically have the same OT as the trainer.
        # After all, if caught, it'll thus be already set.
        # And if not, what will the OT matter?
        self.ot = ot
        
        # ball caught in, as a ???
        # probably will just be a string set to the used ball's display name, but
        # that can be decided when items are
        # ( this might not even see use due to card system )
        self.ball = "basic"
        
        # "met at" statement, as a string
        # displayed as-is, since this doesn't need to hold any real meaning
        # ( might also not see use due to card system )
        self.met = "at an unknown location."
        
        # xt rate, as string
        self.xprate = self.getXPRate()

        # level, as an int
        self.level = level
        
        # experience points, as an int
        self.xp = self.getXPtoLv(self.level) # Give just enough to reach that level.
        
        # Whether the Pokémon starts as an egg.
        self.isEgg = isEgg # This doesn't check if it has previous evolutions or anything. So, if for some insane reason, you want a Charizard egg...
        
        # friendship, as an int
        if self.isEgg:
            self.friendship = 120 # Eggs are decently friendly. This is true to real life, where eggs sometimes dress up in polka-dots.
        else:
            self.friendship = self.getDicEntry('baseHappiness')
        
        # bond, as an int
        # this is assuming that nufusion's fusion mechanics are the same
        # so this might not stick
        self.bond = 0 # Note from Joat: I have no clue what this is. Bulbapedia has no clue what this is. What?
        
        # affection, as an int
        # if bond sticks, this might just be replaced with bond
        self.affection = 0
        
        # moves known, as a dict of dicts
        # each move should have a key of its move data key,
        # with values for current pp and pp ups applied i.e.
        # absorb: {pp: 20, pp_ups: 0}
        # the rest of the data will be drawn from the move data
        # this may just become a list of move keys depending on out-of-battle mechanics
        self.moves = {}
        # movesets, as a list of lists
        # each list should be composed of move keys
        # because of the dynamic nature of python data structures, an arbitrary amount of
        # movesets with 1 to 4 moves could be allowed for each pokemon
        # however, for starting simple, let's just stick to 4 lists of 4 entries,
        # similar to how it's currently done
        self.move_sets = [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        # ivs, as a dict
        # uses the same keys as base stats, for simpler stat calculations
        self.iv = {
            'hp': random.randint(0,31),
            'atk': random.randint(0,31),
            'def': random.randint(0,31),
            'spa': random.randint(0,31),
            'spd': random.randint(0,31),
            'spe': random.randint(0,31)
        }
        # evs, as a dict
        # see note about ivs
        # note that the pokemon's actual stats aren't stored, as they can always be calculated
        # on the fly from ivs, evs, and nature
        self.ev = {
            'hp': 0,
            'atk': 0,
            'def': 0,
            'spa': 0,
            'spd': 0,
            'spe': 0
        }
        
        # hold item, as a ???
        # as of writing, items don't exist nor have a planned way of handling them
        # so for now, this is just a "for future use" thing
        self.hold_item = None
        
        # current hp, as an int, full by default
        self.hp = self.getStat('hp')
        
        # current status, as a ??? (suggestion from Joat: list of dicts, where each status has a name and a duration left)
        # only includes statuses that persist out of battle,
        # like sleep, burn, freeze, etc.
        # this and hp may go unused if pokemon automatically heal after battle
        self.status = None
        
        # current steps for hatching egg, if applicable.
        self.eggSteps = 0
    
    # While mutable traits are stored in the class itself,
    # immutable traits of the species are retrieved here from the Pokedex dictionary.
    # The species parameter is to account for mega evolution.
    def getDic(self, species=None):
        if species == None or species not in dex:
            species = self.species
        # sdic is the dictionary entry for the species.
        sdic = None
        try:
            sdic = dex[species.lower()] # Retrieve the dictionary for the species. lower() is used as a safeguard against programmer error, since uppercase keys do not exist in this dictionary (if they do, they should be corrected).
        except KeyError:
            sdic = dex["missingno"] # If the key is not found, default to missingno.
        return sdic

    # While mutable traits are stored in the class itself,
    # immutable traits of the species are retrieved here from the Pokedex dictionary.
    # The species parameter is to account for mega evolution.
    def getDicEntry(self, keyName, species = None):
        # take into consideration that the stat may not exist outside of the base form
        entry = self.getDic(species).get(keyName)
        if entry is None and keyName != "baseSpecies":
            entry = self.getDic(self.getDicEntry("baseSpecies")).get(keyName)
        # Return the requested dictionary value.
        return entry
    
    # The total XP required to get to the specified level.
    def getXPtoLv(self, level):
        if level == 1: # Level 1 always requires 0XP to get to, for obvious reasons.
            return 0
        if self.xprate == 'erratic':
            if level <= 50:
                return int((level*level*level*(100-level))/50)
            elif level <= 68:
                return int((level*level*level*(150-level))/100)
            elif level <= 98:
                return int((level*level*level*int((1911-(10*level))/3))/100) # Lesson from GameFreak: Don't drink and code, kids.
            else:
                return int((level*level*level*(160-level))/100)
        elif self.xprate == 'fast':
            return int(4*level*level*level/5)
        elif self.xprate == 'mediumfast':
            return level*level*level
        elif self.xprate == 'mediumslow':
            return int((6*level*level*level/5) - (15*level*level) + (100*level) - 140)
        elif self.xprate == 'slow':
            return int(5*level*level*level/4)
        else: # Invalid values for xprate will default to fluctuating.
            if level <= 15:
                return int(level*level*level*((int((level+1)/3)+24)/50))
            elif level <= 36:
                return int(level*level*level*((level+14)/50))
            else:
                return int(level*level*level*((int(level/2)+32)/50))
    
    # HP modification function, for convenience. Species parameter is for megas. And Trix is for kids.
    def modifyHP(self, amount, species = None):
        self.hp += amount # Modify HP.
        if self.hp > self.getStat("HP", species): # Enforce max HP.
            self.hp = self.getStat("HP", species)
        if self.hp < 0: # Enforce non-negative.
            self.hp = 0
     
    # Get the specified stat for the specified species, default own species, adjusted for factors such as level and IV.
    # The species parameter is primarily to account for mega forms, as those are only present in battle.
    def getStat(self, statType, isCrit = False, species = None):
        if species == None or species not in dex:
            species = self.species
        # sdic is the dictionary entry for the species.
        sdic = None
        try:
            sdic = dex[species.lower()] # Retrieve the dictionary for the species. lower() is used as a safeguard against programmer error, since uppercase keys do not exist in this dictionary (if they do, they should be corrected).
        except KeyError:
            sdic = dex["missingno"] # If the key is not found, default to missingno.
        
        # Retrieve the base stat. If the stat does not exist, return 2 as a failsafe. 2 is a stat that couldn't happen normally (outside of combat), so this should set off a red flag if seen in a status screen or the like.
        baseStat = sdic["baseStats"].get(statType)
        if baseStat == None:
            return 2
        
        # Return calculated stat.
        if statType == "hp":
            return int((2 * baseStat + self.iv["hp"] + int(self.ev["hp"]/4)) * self.level / 100) + self.level + 10
        else:
            #TODO: Make sure that isCrit is checked for the temp stat boosts, and debufs as approperate. don't let burn effect it
            natureMod = self.NATURES[self.nature].get(statType, 1)
            return (int((2 * baseStat + self.iv[statType] + int(self.ev[statType]/4)) * self.level / 100) + 5) * natureMod
    
    # Get the name of the active ability.
    # As with getStat, the species parameter is to account for megas.
    def getAbilityName(self, species = None):
        if species == None or species not in dex:
            species = self.species
        # sdic is the dictionary entry for the species.
        sdic = None
        try:
            sdic = dex[species.lower()] # Retrieve the dictionary for the species. lower() is used as a safeguard against programmer error, since uppercase keys do not exist in this dictionary (if they do, they should be corrected).
        except KeyError:
            sdic = dex["missingno"] # If the key is not found, default to missingno.
        return sdic["abilities"].get[self.ability] # Remember, this can be None. Account for this.

    def getName(self):
        if self.nickname is None:
            return self.species
        else:
            return self.nickname
    
    def checkAcc(self):
        #For now return 1, we will need to decide how to store this variable properly.
        return 1
    
    def checkEvade(self):
        #For now return 1, we will need to decide how to store this variable properly.
        return 1

    def checkCrit(self, moveCritRatio = 0):
        """ 
        For now this will just return 0, but have it calculate this later
        1. Start with a variable C and set it to 0.
        2. If the user is a Farfetch'd holding a Stick or a Chansey holding a Lucky Punch, set C to 2. (In G/S/C, no further modifications would be made to C if this was the case.)
        3. If the move has a high critical hit ratio, add 1 to C (2 in G/S/C).
        4. If the user has used Focus Energy or has a Dire Hit used on it since becoming active, add 2 to C (1 in G/S/C).
        5. If the user has had a Dire Hit 2 used on it once, add 1 to C; if it has had a Dire Hit 2 used on it more than once, add 2 to C.
        6. If the user has had a Dire Hit 3 used on it at least once, add 2 to C.
        7. If the user has the ability Super Luck, add 1 to C.
        8. If the user is holding a Scope Lens or a Razor Claw, add 1 to C.
        9. If the user has consumed a Lansat Berry since becoming active, add 2 to C.
        """
        if moveCritRatio is None: 
            moveCritRatio = 0
        C = moveCritRatio
        #TODO: Make this actually do something, going to be touching this later when moves and items are put in.
        return C
    
    def getTypes(self) -> list:
        """return a list containing the types"""
        types = self.getDicEntry("types")
        #TODO: Eventually there will be something that changes what type they are, pull from there instead. Odds are just call the species within the getDicEntry
        return types