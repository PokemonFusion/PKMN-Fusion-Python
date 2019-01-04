import copy, random
from pokemondex import BattlePokedex as dex

class Pokemon:

    class PokeData:
        def __init__(self, species):
            sdic = dex[species]
            self.num = sdic["num"]
            self.species = sdic["species"]
            self.types = sdic["types"]
            self.gender = sdic.get("gender")
            self.genderRatio = self.GenderRatio(sdic.get("genderRatio"))
            self.baseStats = self.BaseStats(sdic["baseStats"])

        class GenderRatio:
            def __init__(self, ratio):
                if ratio is None:
                    self.Male = 0.5
                    self.Female = 0.5
                else:
                    self.Male = ratio["M"]
                    self.Female = ratio["F"]

        class BaseStats:
            def __init__(self, stats):
                #I decided to use words that were less likely to be mistaken for one another.
                #I could see spd and spe getting confused or typoed
                self.HP = stats["hp"]
                self.Atk = stats["atk"]
                self.Def = stats["def"] #def is a reserved name, so having to use Def
                self.SpAtk = stats["spa"]
                self.SpDef = stats["spd"]
                self.Speed = stats["spe"]




    def __init__(self, species = None, nickname = None, gender = None):
        
        self.species = species #must be a pokemon key value
        self.nickname = nickname
        self.gender = gender
        self.pokedata = self.PokeData(species)



    def name(self):
        if self.nickname is None:
            return self.pokedata["species"]
        else:
            return self.nickname

