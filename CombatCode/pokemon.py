import copy, random
from pokemondex import BattlePokedex as dex

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
                if self.genderRatio.get["M"] == None: # Something's wrong if the gender is undefined and genderRatio's "M" is also undefined. Default to "N".
                    self.gender = "N"
                # Randomly set gender according to ratio provided.
                elif random.random() < self.genderRatio["M"]:
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
        
        # level, as an int
        self.level = level
        
        # experience points, as an int
        self.xp = self.getXPtoLv(self.level) # Give just enough to reach that level.
        
        # Whether the Pok�mon starts as an egg.
        self.isEgg = isEgg # This doesn't check if it has previous evolutions or anything. So, if for some insane reason, you want a Charizard egg...
        
        # friendship, as an int
        if self.isEgg:
            self.friendship = 120 # Eggs are decently friendly. This is true to real life, where eggs sometimes dress up in polka-dots.
        else:
            self.friendship = sdic['friendship'] # IMPORTANT: ADD THIS TO THE POKEDEX! Or do some alternate thing.
        
        # bond, as an int
        # this is assuming that nufusion's fusion mechanics are the same
        # so this might not stick
        self.bond = 0 # Note from Joat: I have no clue what this is. Bulbapedia has no clue what this is. What?
        
        # affection, as an int
        # if bond sticks, this might just be replaced with bond
        self.affection = 0,
        
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
    def getDicEntry(self, keyName, species = None):
        if species == None or species not in dex:
            species = self.species
        # sdic is the dictionary entry for the species.
        sdic = None
        try:
            sdic = dex[species.lower()] # Retrieve the dictionary for the species. lower() is used as a safeguard against programmer error, since uppercase keys do not exist in this dictionary (if they do, they should be corrected).
        except KeyError:
            sdic = dex["missingno"] # If the key is not found, default to missingno.
        # Return the requested dictionary value.
        return sdic.get(keyName)
    
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
    
    # Get the damage for the move.
    # With critMod, 1 is non-crit, 2 is crit.
    # Critical hits should NOT be determined with this function.
    # The reason is, using this function to determine that would make it hard to know
    # whether or not to display the crit message.
    # The default value for critMod is temporary. In the final version, it should be required to specify.
    # species parameter is to account for megas.
    def getMoveDamage(self, move, defender, critMod = 1, species = None, defenderSpecies = None):
        if species == None or species not in dex:
            species = self.species
        damage = (((2*self.level)/5+2) * move.power * self.getStat("atk", species) / defender.getStat("def", defenderSpecies) / 50 + 2) # Initialize damage based on move power, attack, defense, and level.
        # TODO: Adjust based on number targeted.
        # TODO: Adjust based on weather.
        # TODO: Adjust based on badge.
        damage *= critMod # Adjust for critical.
        damage = int(damage*random.uniform(0.85, 1.0)) # Randomize.
        if move.type in self.getDicEntry("types", species): # Adjust for STAB.
            if self.getAbilityName(species) == "adaptability":
                damage *= 2
            else:
                damage *= 1.5
        # TODO: Adjust for type (dis)advantage.
        # TODO: Adjust for Burn.
        # TODO: Adjust for misc. other factors.
    
    # Get the specified stat for the specified species, default own species, adjusted for factors such as level and IV.
    # The species parameter is primarily to account for mega forms, as those are only present in battle.
    def getStat(self, statType, species = None):
        if species == None or species not in dex:
            species = self.species
        # sdic is the dictionary entry for the species.
        sdic = None
        try:
            sdic = dex[species.lower()] # Retrieve the dictionary for the species. lower() is used as a safeguard against programmer error, since uppercase keys do not exist in this dictionary (if they do, they should be corrected).
        except KeyError:
            sdic = dex["missingno"] # If the key is not found, default to missingno.
        
        # Retrieve the base stat. If the stat does not exist, return 2 as a failsafe. 2 is a stat that couldn't happen normally (outside of combat), so this should set off a red flag if seen in a status screen or the like.
        baseStat = sdic["baseStats"].get[statType]
        if baseStat == None:
            return 2
        
        # Return calculated stat.
        if statType == "hp":
            return int((2 * baseStat + self.iv[baseStat] + int(self.ev[baseStat]/4)) * self.level / 100) + self.level + 10
        else:
            natureMod = self.NATURES[self.nature].get(statType, 1)
            return (int((2 * baseStat + self.iv[baseStat] + int(self.ev[baseStat]/4)) * self.level / 100) + 5) * natureMod
    
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
            return self.pokedata.species
        else:
            return self.nickname
