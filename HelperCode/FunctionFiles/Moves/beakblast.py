def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('beakblast');
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Beak Blast');
			}
	""" 
	pass

def onHit (pokemon, source, move):
	"""function (pokemon, source, move) {
				if (move.flags['contact']) {
					source.trySetStatus('brn', pokemon);
				}
			}
	""" 
	pass

def onMoveAborted (pokemon):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass

def onAfterMove (pokemon):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass