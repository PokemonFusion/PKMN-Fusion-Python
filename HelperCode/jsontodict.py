import json, sys, os
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join('')))

pokemon_files = ['moves.json', 'items.json', 'pokemon.json', 'abilities.json']
pokemon_export = ['movesdict.py', 'itemsdict.py', 'pokemondict.py', 'abilitiesdict.py']
pokemon_dictname = ['BattleMovedex', "BattleItems", "PokemonDex", "BattleAbilities"]

# Abilities has an issue with converting, but you can do it manually, just rename true to True, false to False, and
# make sure it's structured like a dictionary

for i in range(len(pokemon_files)):
	with open(pokemon_files[i]) as json_file:
		data = json.load(json_file, encoding='UTF-8')
		with open(pokemon_export[i], "w+") as filename:
			filename.write(pokemon_dictname[i] + " = ")
			pprint(data, stream=filename)

