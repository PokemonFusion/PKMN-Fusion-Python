import random
from math import floor
from pokeglobals import Moves

"""
 Assumptions:

 The current version will be using a dictionary for the data

 Current template:

 BattleData = { "teams" : { "A" : { 1 : {*Pokemon information/stats*}} },
                "battle" : {},
                "turn" : { "position" : { "field-A1" : 1  } }
 }

 Update: 11/28/2018
    Decided to go with a class instead of a dictionary the class is in the battledata.py file


"""


def accuracy_check(attacker, target, move) -> bool:
    """This will return if an attack hits or misses the target"""
    #place holders, but we will want to use classes for each properly
    attacc = attacker.checkacc()
    tareva = target.checkevade()
    moveacc = move.accuracy
    tohit = moveacc * (attacc/tareva)
    hitroll = random.random()
    if tohit <= hitroll:
        return True
    else:
        return False



def critical_hit_check() -> bool:
    """This will return if an attack is a crit or a miss"""
    pass


def base_damage(level, basePower, attackStat, defenseStat) -> int:
    """Damage before modifiers"""
    damage = ((((((2 * level) / 5) + 2) * basePower * (attackStat * 1.0) /
                defenseStat) / 50) + 2)
    randMod = random.randint(85, 100)/100.0
    return int(damage * randMod)
