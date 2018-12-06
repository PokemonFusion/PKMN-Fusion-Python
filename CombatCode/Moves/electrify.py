def onTryHit (target):
	"""function (target) {
			if (!this.willMove(target) && target.activeTurns) return false;
		}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-singleturn', target, 'move: Electrify');
			}
	""" 
	pass

def onModifyMove (move):
	"""function (move) {
				this.debug('Electrify making move type electric');
				move.type = 'Electric';
			}
	""" 
	pass