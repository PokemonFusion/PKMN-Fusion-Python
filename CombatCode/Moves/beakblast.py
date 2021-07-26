def beforeTurnCallback(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('beakblast');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Beak Blast');
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (pokemon, source, move) {
				if (move.flags['contact']) {
					source.trySetStatus('brn', pokemon);
				}
			}
	""" 
	pass

def onMoveAborted(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass

def onAfterMove(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass
