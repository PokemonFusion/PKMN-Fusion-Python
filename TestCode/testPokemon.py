import sys
import os

sys.path.append(os.path.abspath(os.path.join('')))
sys.path.append(os.path.abspath('../CombatCode'))
from pokemon import Pokemon
from pokemonCombinedDex import BattlePokedex as dex
from pokemon import teamGeneration as teamGen

# tp = Pokemon(1,'thundurus', level=35)

pokemon = []

for poke in dex:
    print(poke.title())
    pokemon.append(Pokemon(1, poke, level=50))


for poke in pokemon:
    team = teamGen(False, [[poke.getName(), poke.level]])
    print(team[0].getName() + ", " + str(team[0].move_sets[0][0]))
