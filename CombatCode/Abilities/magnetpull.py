def onFoeTrapPokemon (pokemon):
	"""function (pokemon) {
			if (pokemon.hasType('Steel') && this.isAdjacent(pokemon, this.effectData.target)) {
				pokemon.tryTrap(true);
			}
		}
	""" 
	pass

def onFoeMaybeTrapPokemon (pokemon, source):
	"""function (pokemon, source) {
			if (!source) source = this.effectData.target;
			if ((!pokemon.knownType || pokemon.hasType('Steel')) && this.isAdjacent(pokemon, source)) {
				pokemon.maybeTrapped = true;
			}
		}
	""" 
	pass