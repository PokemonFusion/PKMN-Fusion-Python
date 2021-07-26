import random
import sys, os
from CombatCode.learnset_code import level_moves as lm

sys.path.append(os.path.abspath(os.path.join('')))
sys.path.append(os.path.abspath('../CombatCode'))
from CombatCode.pokemonCombinedDex import BattlePokedex as dex

# dict of all the natures and their stat bonuses
# there's nothing preventing the addition of natures that modify hp,
# or more than two stats, or have a different bonuses from +10% and -10%.
# This is static.
NATURES = {
    "Hardy": {},
    "Lonely": {'atk': 1.1, 'def': 0.9},
    "Brave": {'atk': 1.1, 'spe': 0.9},
    "Adamant": {'atk': 1.1, 'spa': 0.9},
    "Naughty": {'atk': 1.1, 'spd': 0.9},
    "Bold": {'def': 1.1, 'atk': 0.9},
    "Docile": {},
    "Relaxed": {'def': 1.1, 'spe': 0.9},
    "Impish": {'def': 1.1, 'spa': 0.9},
    "Lax": {'def': 1.1, 'spd': 0.9},
    "Timid": {'spe': 1.1, 'atk': 0.9},
    "Hasty": {'spe': 1.1, 'def': 0.9},
    "Serious": {},
    "Jolly": {'spe': 1.1, 'spa': 0.9},
    "Naive": {'spe': 1.1, 'spd': 0.9},
    "Modest": {'spa': 1.1, 'atk': 0.9},
    "Mild": {'spa': 1.1, 'def': 0.9},
    "Quiet": {'spa': 1.1, 'spe': 0.9},
    "Bashful": {},
    "Rash": {'spa': 1.1, 'spd': 0.9},
    "Calm": {'spd': 1.1, 'atk': 0.9},
    "Gentle": {'spd': 1.1, 'def': 0.9},
    "Sassy": {'spd': 1.1, 'spe': 0.9},
    "Careful": {'spd': 1.1, 'spa': 0.9},
    "Quirky": {},
}

STATUSES = {
    0: "Normal",
    1: "Burn",
    2: "Freeze",
    3: "Paralysis",
    4: "Poison",
    5: "Sleep",
    6: "Toxic"
}
STATUSES_SHORT = {
    0: "NRM",
    1: "BRN",
    2: "FRZ",
    3: "PAR",
    4: "PSN",
    5: "SLP",
    6: "TOX"
}

STATUSES_REVERSE_SHORT = {
    "NRM": 0,
    "BRN": 1,
    "FRZ": 2,
    "PAR": 3,
    "PSN": 4,
    "SLP": 5,
    "TOX": 6
}

class Pokemon:

    # Get the XP Rate of the pokemon in question.
    def getXPRate(self):
        rate = self.getDicEntry("growthRateId")

        ratedict = {
            1: "slow",
            2: "mediumfast",
            3: "fast",
            4: "mediumslow",
            5: "erratic",
            6: "fluctuating"
        }
        return ratedict.get(rate)

    def __init__(self, ot, species="missingno", nickname=None, gender=None, isEgg=False, level=1,
                 ability=random.choice(["0", "1"])):

        # Pokemon species, as a dict key
        # this should always be set in actual Pokemon, as a lot of info is derived directly
        # from species definitions
        self.species = species

        # the pokemon's nickname, as a string
        # if None, then the displayed name should be the species's display name
        self.nickname = nickname

        # gender as a string
        # like in species definitions, should be 'M', 'F', or 'N'
        if gender is not None:  # If the gender is provided, just use that.
            self.gender = gender
        else:  # Otherwise, choose a random valid gender.
            self.gender = self.getDicEntry("gender")  # Set gender to default value, if there is one.
            if self.gender is None:  # If there isn't, randomize it.
                genderRatio = self.getDicEntry("genderRatio")  # Temporary variable to assist in determining gender.
                # if no gender ratio is found, it's 50/50
                if genderRatio is None:
                    self.gender = random.choice(["M", "F"])
                # Randomly set gender according to ratio provided.
                elif random.random() < genderRatio["M"]:
                    self.gender = "M"
                else:
                    self.gender = "F"

        # nature, as a string
        self.nature = random.choice(list(NATURES.keys()))

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
        self.xp = self.getXPtoLv(self.level)  # Give just enough to reach that level.

        # Whether the Pokémon starts as an egg.
        self.isEgg = isEgg  # This doesn't check if it has previous evolutions or anything. So, if for some insane
        # reason, you want a Charizard egg...

        # friendship, as an int
        if self.isEgg:
            self.friendship = 120  # Eggs are decently friendly. This is true to real life, where eggs sometimes
            # dress up in polka-dots.
        else:
            self.friendship = self.getDicEntry('baseHappiness')

        # bond, as an int
        # this is assuming that nufusion's fusion mechanics are the same
        # so this might not stick
        self.bond = 0  # Note from Joat: I have no clue what this is. Bulbapedia has no clue what this is. What?

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
            'hp': random.randint(0, 31),
            'atk': random.randint(0, 31),
            'def': random.randint(0, 31),
            'spa': random.randint(0, 31),
            'spd': random.randint(0, 31),
            'spe': random.randint(0, 31)
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
        # This is where we will be storing stat mods, we will need to make sure that they don't go outside of +-6
        self.statMods = {
            'atk': 0,
            'def': 0,
            'spa': 0,
            'spd': 0,
            'spe': 0,
            'acc': 0,
            'eva': 0
        }

        # hold item, as a ???
        # as of writing, items don't exist nor have a planned way of handling them
        # so for now, this is just a "for future use" thing
        self.hold_item = None

        # current hp, as an int, full by default
        self.hp = self.getStat('hp')

        # current status, as a ???
        # (suggestion from Joat: list of dicts, where each status has a name and a duration left)
        # only includes statuses that persist out of battle,
        # like sleep, burn, freeze, etc.
        # this and hp may go unused if pokemon automatically heal after battle
        self.status = {"name": 0, "duration": 0}  # these are the default values

        # current steps for hatching egg, if applicable.
        self.eggSteps = 0

    # While mutable traits are stored in the class itself,
    # immutable traits of the species are retrieved here from the Pokedex dictionary.
    # The species parameter is to account for mega evolution.
    def getDic(self, species=None):
        if species is None or species not in dex:
            species = self.species
        # sdic is the dictionary entry for the species.
        try:
            sdic = dex[
                species.lower()]  # Retrieve the dictionary for the species. lower() is used as a safeguard against
            # programmer error, since uppercase keys do not exist in this dictionary (if they do, they should be
            # corrected).
        except KeyError:
            sdic = dex["missingno"]  # If the key is not found, default to missingno.
        return sdic

    # While mutable traits are stored in the class itself,
    # immutable traits of the species are retrieved here from the Pokedex dictionary.
    # The species parameter is to account for mega evolution.
    def getDicEntry(self, keyName, species=None):
        # take into consideration that the stat may not exist outside of the base form
        entry = self.getDic(species).get(keyName)
        if entry is None and keyName != "baseSpecies":
            entry = self.getDic(self.getDicEntry("baseSpecies")).get(keyName)
        # Return the requested dictionary value.
        return entry

    # The total XP required to get to the specified level.
    def getXPtoLv(self, level):
        if level == 1:  # Level 1 always requires 0XP to get to, for obvious reasons.
            return 0
        if self.xprate == 'erratic':
            if level <= 50:
                return int((level * level * level * (100 - level)) / 50)
            elif level <= 68:
                return int((level * level * level * (150 - level)) / 100)
            elif level <= 98:
                return int((level * level * level * int(
                    (1911 - (10 * level)) / 3)) / 100)  # Lesson from GameFreak: Don't drink and code, kids.
            else:
                return int((level * level * level * (160 - level)) / 100)
        elif self.xprate == 'fast':
            return int(4 * level * level * level / 5)
        elif self.xprate == 'mediumfast':
            return level * level * level
        elif self.xprate == 'mediumslow':
            return int((6 * level * level * level / 5) - (15 * level * level) + (100 * level) - 140)
        elif self.xprate == 'slow':
            return int(5 * level * level * level / 4)
        else:  # Invalid values for xprate will default to fluctuating.
            if level <= 15:
                return int(level * level * level * ((int((level + 1) / 3) + 24) / 50))
            elif level <= 36:
                return int(level * level * level * ((level + 14) / 50))
            else:
                return int(level * level * level * ((int(level / 2) + 32) / 50))

    # HP modification function, for convenience. Species parameter is for megas. And Trix is for kids.
    def modifyHP(self, amount, species=None):
        self.hp += amount  # Modify HP.
        if self.hp > self.getStat("hp", species):  # Enforce max HP.
            self.hp = self.getStat("hp", species)
        if self.hp < 0:  # Enforce non-negative.
            self.hp = 0

    # Get the specified stat for the specified species, default own species, adjusted for factors such as level and IV.
    # The species parameter is primarily to account for mega forms, as those are only present in battle.
    def getStat(self, statType, isCrit=False, species=None):
        """Use this to get a stat, hp, atk, def, spa, spd, spe
        isCrit - if a critical happened
        species - force a species name"""
        statType = statType.lower()  # force the name to lower to make sure it doesn't blow up.
        # Retrieve the base stat. If the stat does not exist, return 2 as a failsafe. 2 is a stat that couldn't
        # happen normally (outside of combat), so this should set off a red flag if seen in a status screen or the
        # like.
        baseStat = self.getDicEntry("baseStats", species=species).get(statType, 2)

        # Return calculated stat.
        if statType == "hp":
            return int((2 * baseStat + self.iv["hp"] + int(self.ev["hp"] / 4)) * self.level / 100) + self.level + 10
        else:
            # TODO: Make sure that isCrit is checked for the temp stat boosts, and debuffs as appropriate.
            #  Burn halving attack should still happen
            #  (Correction: Burn halves /damage/ of physical moves, not attack stat anymore)
            #  Paralysis should decrease speed by half

            if isCrit:
                critbonus = 1.5
            else:
                critbonus = 1

            if isCrit and ((self.statMods[statType] < 0 and statType in ['atk', 'spa']) or
                           (self.statMods[statType] > 0 and statType in ['def', 'spd'])):
                statmod = 1
            else:
                statmod = self.getStatMod(statType)

            natureMod = NATURES[self.nature].get(statType, 1)

            stat = int((int(
                (2 * baseStat + self.iv[statType] + int(self.ev[statType] / 4)) * self.level / 100) + 5) * natureMod
                       * statmod * critbonus)

            if self.status["name"] == 3 and statType == 'spd' and self.getAbilityName() != "Quick Feet":
                stat = stat / 2

            return stat

    def getStatMod(self, stat: str) -> float:
        """This will return the stat mod of the multiplier involved.
        The calculations for eva and acc are going to be different
        """

        statmult = {
            -6: 2 / 8,
            -5: 2 / 7,
            -4: 2 / 6,
            -3: 2 / 5,
            -2: 2 / 4,
            -1: 2 / 3,
            0: 2 / 2,
            1: 3 / 2,
            2: 4 / 2,
            3: 5 / 2,
            4: 6 / 2,
            5: 7 / 2,
            6: 8 / 2
        }
        evaaccmult = {
            -6: 3 / 9,
            -5: 3 / 8,
            -4: 3 / 7,
            -3: 3 / 6,
            -2: 3 / 5,
            -1: 3 / 4,
            0: 3 / 3,
            1: 4 / 3,
            2: 5 / 3,
            3: 6 / 3,
            4: 7 / 3,
            5: 8 / 3,
            6: 9 / 3
        }

        if stat is not None and stat in self.statMods:
            # Make sure the value is between -6 and 6
            if self.statMods[stat] > 6:
                self.statMods[stat] = 6
            if self.statMods[stat] < -6:
                self.statMods[stat] = -6

            if stat == 'acc':
                return evaaccmult[self.statMods[stat]]
            elif stat == 'eva':
                # eva is the inverse stat value of acc
                return evaaccmult[self.statMods[stat] * -1]
            else:
                return statmult[self.statMods[stat]]

        else:
            return 1

    # Get the name of the active ability.
    # As with getStat, the species parameter is to account for megas.
    def getAbilityName(self, species=None):
        if species is None or species not in dex:
            species = self.species
        # sdic is the dictionary entry for the species.
        try:
            sdic = dex[
                species.lower()]
            # Retrieve the dictionary for the species. lower() is used as a
            # safeguard against programmer error, since uppercase keys do not
            # exist in this dictionary (if they do, they should be corrected).
        except KeyError:
            sdic = dex["missingno"]  # If the key is not found, default to missingno.
        return sdic["abilities"].get[self.ability]  # Remember, this can be None. Account for this.

    def getName(self):
        if self.nickname is None:
            return self.species.title()
        else:
            return self.nickname

    def checkAcc(self):
        # For now return 1, we will need to decide how to store this variable properly.
        return self.getStatMod('acc')

    def checkEvade(self):
        # For now return 1, we will need to decide how to store this variable properly.
        return self.getStatMod('eva')

    def checkCrit(self, moveCritRatio=0):
        """ 
        For now this will just return 0, but have it calculate this later
        1. Start with a variable C and set it to 0.
        2. If the user is a Farfetch'd holding a Stick or a Chansey holding a Lucky Punch, set C to 2. (In G/S/C, no
           further modifications would be made to C if this was the case.)
        3. If the move has a high critical hit ratio, add 1 to C (2 in G/S/C).
        4. If the user has used Focus Energy or has a Dire Hit used on it since becoming active, add 2 to C (1 in G/S/C).
        5. If the user has had a Dire Hit 2 used on it once, add 1 to C; if it has had a Dire Hit 2 used on it more
           than once, add 2 to C.
        6. If the user has had a Dire Hit 3 used on it at least once, add 2 to C.
        7. If the user has the ability Super Luck, add 1 to C.
        8. If the user is holding a Scope Lens or a Razor Claw, add 1 to C.
        9. If the user has consumed a Lansat Berry since becoming active, add 2 to C.
        """
        if moveCritRatio is None:
            moveCritRatio = 0
        C = moveCritRatio
        # TODO: Make this actually do something, going to be touching this later when moves and items are put in.
        return C

    def getTypes(self) -> list:
        """return a list containing the types"""
        types = self.getDicEntry("types")
        # TODO: Eventually there will be something that changes what type they are, pull from there instead.
        #  Odds are just call the species within the getDicEntry
        # This function needs to exist, there are some abilities/moves/items that modify type that isn't just
        # changing it to a different pokemon
        return types

    def takeDamage(self, damage, species=None) -> int:
        """Take damage and return current hp"""
        self.modifyHP(damage * -1, species=species)
        return self.hp

    def getItem(self) -> str:
        """In case we have other ways to handle holding items, like temp items"""
        return self.hold_item

    def __repr__(self):
        return f"{self.getName()} - {hex(id(self))}"

    def getStatusName(self, short=False) -> str:

        if short:
            statdic = STATUSES_SHORT
        else:
            statdic = STATUSES

        return statdic[self.status["name"]]


def teamGeneration(specify=False, team=None):
    # specify   - If the moves and abilities should be specified or not
    # team      - List of lists for the team: [['name', lvl], ... ]
    fullTeam = []
    if team is None:
        return
    if len(team) > 0:
        count = len(team) + 1
        i = 0
        while i < count - 1:
            moveIndex = 0
            teamPoke = Pokemon(0, team[i][0], None, None, False, team[i][1])
            pokeMoves = lm(team[i][0], team[i][1])
            for m in range(0, team[i][1]):
                if moveIndex == 4:
                    break
                try:
                    n = 0
                    while n < len(pokeMoves[team[i][1] - m]):
                        teamPoke.move_sets[0][0][moveIndex] = pokeMoves[team[i][1] - m][n]
                        moveIndex += 1
                        n += 1
                        if moveIndex == 4:
                            break
                except KeyError as e:
                    continue
                except IndexError as e:
                    continue
            fullTeam.append(teamPoke)
            i += 1
    return fullTeam
