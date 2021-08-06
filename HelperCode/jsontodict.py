import json, sys, os
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join('')))

pokemon_files = ['moves.json', 'items.json', 'pokemon.json', 'abilities.json']
pokemon_export = ['movesdict.py', 'itemsdict.py', 'pokemondict.py', 'abilitiesdict.py']
pokemon_dictname = ['BattleMovedex', "BattleItems", "PokemonDex", "BattleAbilities"]

for i in range(pokemon_files.count()):
	with open(pokemon_files[i]) as json_file:
		data = json.load(json_file)
		with open(pokemon_export[i], "w+") as filename:
			filename.write(pokemon_dictname[i] + " = ")
			pprint(data, stream=filename)