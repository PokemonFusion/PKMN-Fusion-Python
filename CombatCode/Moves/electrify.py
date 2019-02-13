def onTryHit(datadic : dict):
	"""function (target) {
			if (!this.willMove(target) && target.activeTurns) return false;
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target) {
				this.add('-singleturn', target, 'move: Electrify');
			}
	""" 
	pass

def onModifyMove(datadic : dict):
	"""function (move) {
				this.debug('Electrify making move type electric');
				move.type = 'Electric';
			}
	""" 
	pass
