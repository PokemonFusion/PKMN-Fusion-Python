def onStart(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('truant');
			if (pokemon.activeTurns && (pokemon.moveThisTurnResult !== undefined || !this.queue.willMove(pokemon))) {
				pokemon.addVolatile('truant');
			}
		}
	""" 
	pass

def onBeforeMove(**bvalues):
	"""function (pokemon) {
			if (pokemon.removeVolatile('truant')) {
				this.add('cant', pokemon, 'ability: Truant');
				return False;
			}
			pokemon.addVolatile('truant');
		}
	""" 
	pass
