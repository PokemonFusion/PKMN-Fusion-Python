def onFoeTrapPokemon (pokemon):
	"""function (pokemon) {
			if (!pokemon.isAdjacent(this.effectState.target))
				return;
			if (pokemon.isGrounded()) {
				pokemon.tryTrap(True);
			}
		}
	""" 
	pass

def onFoeMaybeTrapPokemon (pokemon, source):
	"""function (pokemon, source) {
			if (!source)
				source = this.effectState.target;
			if (!source || !pokemon.isAdjacent(source))
				return;
			if (pokemon.isGrounded(!pokemon.knownType)) { // Negate immunity if the type is unknown
				pokemon.maybeTrapped = True;
			}
		}
	""" 
	pass