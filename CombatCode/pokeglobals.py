import copy
from CombatCode.battlemovedex import BattleMovedex


def keycheck(dictionary, subdictionary, key) -> object:
    if key in dictionary[subdictionary]:
        return dictionary[subdictionary][key]
    else:
        return None


class Result:
    def __init__(self):
        self.debug = dict()
        self.fainted = list()
        self.text = ""


class Moves:

    def __init__(self, move: str):
        def movecheck(key):
            return keycheck(BattleMovedex, move, key)
        
        self.num = movecheck("num")
        self.accuracy = movecheck("accuracy")
        self.basePower = movecheck("basePower")
        self.category = movecheck("category")
        self.desc = movecheck("desc")
        self.shortDesc = movecheck("shortDesc")
        self.id = movecheck("id")
        self.name = movecheck("name")
        self.pp = movecheck("pp")
        self.priority = movecheck("priority")
        self.flags = movecheck("flags")
        self.secondary = movecheck("secondary")
        self.self = movecheck("self")
        self.target = movecheck("target")
        self.type = movecheck("type")
        self.zMovePower = movecheck("zMovePower")
        self.contestType = movecheck("contestType")
        self.multihit = movecheck("multihit")
        self.boosts = movecheck("boosts")
        self.isViable = movecheck("isViable")
        self.isZ = movecheck("isZ")
        self.onHit = movecheck("onHit")
        self.onModifyMove = movecheck("onModifyMove")
        self.critRatio = movecheck("critRatio")

    def calculateBasePower(self) -> int:
        """
        you'll need to check basePowerCallback and onBasePower
        """
        #for now, just pass the basepower
        return self.basePower

    def __repr__(self):
        return "{}. {}".format(self.num,self.name)
