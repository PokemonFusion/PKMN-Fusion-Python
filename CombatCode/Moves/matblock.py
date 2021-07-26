def onTryHitSide(**bvalues):
	"""function (side, source) {
			if (source.activeTurns > 1) {
				this.add('-hint', "Mat Block only works on your first turn out.");
				return false;
			}
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source) {
				this.add('-singleturn', source, 'Mat Block');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				if (!move.flags['protect']) {
					if (move.isZ) move.zBrokeProtect = true;
					return;
				}
				if (move && (move.target === 'self' || move.category === 'Status')) return;
				this.add('-activate', target, 'move: Mat Block', move.name);
				source.moveThisTurnResult = true;
				let lockedmove = source.getVolatile('lockedmove');
				if (lockedmove) {
					// Outrage counter is reset
					if (source.volatiles['lockedmove'].duration === 2) {
						delete source.volatiles['lockedmove'];
					}
				}
				return null;
			}
	""" 
	pass
