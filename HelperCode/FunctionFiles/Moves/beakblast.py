def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('beakblast');
		}
	""" 
	pass

def onHit (target, source, move):
	"""function (target, source, move) {
				if (this.checkMoveMakesContact(move, source, target)) {
					source.trySetStatus('brn', target);
				}
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Beak Blast');
			}
	""" 
	pass

def onAfterMove (pokemon):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass