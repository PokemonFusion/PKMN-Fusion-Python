def onTryHit(**bvalues):
	"""function (target) {
			if (!this.willMove(target) && target.activeTurns) return false;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-singleturn', target, 'move: Electrify');
			}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move) {
				this.debug('Electrify making move type electric');
				move.type = 'Electric';
			}
	""" 
	pass
