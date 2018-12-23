import pokemondict as poke
import pokemondex as dex
import random

# this is just something for testing pokedict functionality

for x in range(0, 100):
    pokemon = poke.create_pokemon(random.choice(list(dex.BattlePokedex)), level = 50, ability = 'H')

    for k, v in pokemon.items():
        print(k, v)
        
    print("stats", poke.get_pokemon_stats(pokemon))
    print("real ability", poke.get_pokemon_ability(pokemon))
