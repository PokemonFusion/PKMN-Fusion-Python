def onTryHitSide(datadic : dict):
	"""function (side, source) {
			return !!this.willAct();
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target, source) {
				this.add('-singleturn', source, 'Crafty Shield');
			}
	""" 
	pass

def onTryHit(datadic : dict):
	"""function (target, source, move) {
				if (move && (move.target === 'self' || move.category !== 'Status')) return;
				this.add('-activate', target, 'move: Crafty Shield');
				source.moveThisTurnResult = true;
				return null;
			}
	""" 
	pass
