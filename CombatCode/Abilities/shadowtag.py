def onFoeTrapPokemon(**bvalues):
	"""function (pokemon) {
			if (!pokemon.hasAbility('shadowtag') && pokemon.isAdjacent(this.effectState.target)) {
				pokemon.tryTrap(True);
			}
		}
	""" 
	pass

def onFoeMaybeTrapPokemon(**bvalues):
	"""function (pokemon, source) {
			if (!source)
				source = this.effectState.target;
			if (!source || !pokemon.isAdjacent(source))
				return;
			if (!pokemon.hasAbility('shadowtag')) {
				pokemon.maybeTrapped = True;
			}
		}
	""" 
	pass
