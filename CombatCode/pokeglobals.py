import copy
from moves import BattleMoveDex

def keycheck(dictionary, subdictionary, key) -> object:
    if key in dictionary[subdictionary]:
        return dictionary[subdictionary][key]
    else:
        return None


class Moves:

    def __init__(self, move: str):
        def movecheck(key):
            return keycheck(BattleMoveDex, move, key)
        
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