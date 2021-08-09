def beforeTurnCallback(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('beakblast');
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
				if (this.checkMoveMakesContact(move, source, target)) {
					source.trySetStatus('brn', target);
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Beak Blast');
		}
	""" 
	pass

def onAfterMove(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('beakblast');
		}
	""" 
	pass
