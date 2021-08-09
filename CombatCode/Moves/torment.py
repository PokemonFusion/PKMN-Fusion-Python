def onDisableMove(**bvalues):
	"""function (pokemon) {
				if (pokemon.lastMove && pokemon.lastMove.id !== 'struggle')
					pokemon.disableMove(pokemon.lastMove.id);
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Torment');
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				if (pokemon.volatiles['dynamax']) {
					delete pokemon.volatiles['torment'];
					return false;
				}
				this.add('-start', pokemon, 'Torment');
			}
	""" 
	pass
