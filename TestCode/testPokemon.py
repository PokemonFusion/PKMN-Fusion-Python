import sys, os
sys.path.append(os.path.abspath(os.path.join('')))
from CombatCode.pokemon import Pokemon
from CombatCode.pokemonCombinedDex import BattlePokedex as dex



#tp = Pokemon(1,'thundurus', level=35)

pokemon = []

for poke in dex:
    print(poke.title())
    pokemon.append(Pokemon(1,poke, level=50))