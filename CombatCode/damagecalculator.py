import random
from math import floor
from CombatCode.pokemondex import BattlePokedex

"""
 Assumptions:

 The current version will be using a dictionary for the data

 Current template:

 BattleData = { "teams" : { "A" : { 1 : {*Pokemon information/stats*}} },
                "battle" : {},
                "turn" : { "position" : { "field-A1" : 1  } }

 }

"""
def base_damage(level, basePower, attackStat, defenseStat):
    #damage before modifiers
    damage = ((((((2 * level)/ 5) + 2) * basePower * (attackStat * 1.0) / defenseStat) / 50 ) + 2)
    randMod = random.randint(85,100)/100.0
    return int(damage * randMod)
