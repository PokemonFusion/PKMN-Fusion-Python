def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-start', pokemon, 'move: No Retreat');
			}
	""" 
	pass

def onTrapPokemon(**bvalues):
	"""function (pokemon) {
				pokemon.tryTrap();
			}
	""" 
	pass

def onTry(**bvalues):
	"""function (source, target, move) {
			if (source.volatiles['noretreat'])
				return false;
			if (source.volatiles['trapped']) {
				delete move.volatileStatus;
			}
		}
	""" 
	pass
