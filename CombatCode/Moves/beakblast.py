def beforeTurnCallback(datadic : dict):
	"""function (pokemon) {
			pokemon.addVolatile('beakblast');
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Beak Blast');
			}
	""" 
	pass

def onHit(datadic : dict):
	"""function (pokemon, source, move) {
				if (move.flags['contact']) {
					source.trySetStatus('brn', pokemon);
				}
			}
	""" 
	pass

def onMoveAborted(datadic : dict):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass

def onAfterMove(datadic : dict):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass
