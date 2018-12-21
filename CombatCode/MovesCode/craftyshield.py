def onTryHitSide (side, source):
	"""function (side, source) {
			return !!this.willAct();
		}
	""" 
	pass

def onStart (target, source):
	"""function (target, source) {
				this.add('-singleturn', source, 'Crafty Shield');
			}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
				if (move && (move.target === 'self' || move.category !== 'Status')) return;
				this.add('-activate', target, 'move: Crafty Shield');
				source.moveThisTurnResult = true;
				return null;
			}
	""" 
	pass