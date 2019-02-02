import sys, os
sys.path.append(os.path.abspath(os.path.join('')))
from CombatCode.pokemon import Pokemon
from CombatCode.pokeglobals import Moves, Result
from CombatCode.damagecalculator import damage_calc
t1 = Pokemon(1, "pikachu", level=50)
t2 = Pokemon(1, "geodude", level=50)
move = Moves('tackle')

result = damage_calc(t1, t2, move)
