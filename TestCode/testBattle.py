import sys
import os

sys.path.append(os.path.abspath(os.path.join('')))
sys.path.append(os.path.abspath('../CombatCode'))
from battledata import Pokemon
from pokeglobals import Moves, Result
from damagecalculator import damage_calc

t1 = Pokemon(1, "A", 1, "geodude", level=50)
t2 = Pokemon(1, "B", 1, "pikachu", level=50)
move = Moves('tackle')

for x in range(2):
    result = damage_calc(t1, t2, move)
    print(result.text)
    print(result.debug["hp_percent"])
    result = damage_calc(t2, t1, move)
    print(result.text)
    print(result.debug["hp_percent"])
