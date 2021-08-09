def onModifyType(**bvalues):
	"""function (move) {
				if (move.id !== 'struggle') {
					this.debug('Electrify making move type electric');
					move.type = 'Electric';
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-singleturn', target, 'move: Electrify');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (!this.queue.willMove(target) && target.activeTurns)
				return false;
		}
	""" 
	pass
