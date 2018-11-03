import random
from math import floor
from pokemondex import BattlePokedex

print BattlePokedex["pikachu"]["abilities"]
def BaseDamage(level, basePower, attackStat, defenseStat):
    #damage before modifiers
    damage = ((((((2 * level)/ 5) + 2) * basePower * (attackStat * 1.0) / defenseStat) / 50 ) + 2)
    randMod = random.randint(85,100)/100.0
    return int(damage * randMod)
