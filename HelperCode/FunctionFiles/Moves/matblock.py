def onSideStart (target, source):
	"""function (target, source) {
				this.add('-singleturn', source, 'Mat Block');
			}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
				if (!move.flags['protect']) {
					if (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))
						return;
					if (move.isZ || move.isMax)
						target.getMoveHitData(move).zBrokeProtect = true;
					return;
				}
				if (move && (move.target === 'self' || move.category === 'Status'))
					return;
				this.add('-activate', target, 'move: Mat Block', move.name);
				var lockedmove = source.getVolatile('lockedmove');
				if (lockedmove) {
					// Outrage counter is reset
					if (source.volatiles['lockedmove'].duration === 2) {
						delete source.volatiles['lockedmove'];
					}
				}
				return this.NOT_FAIL;
			}
	""" 
	pass

def onTry (source):
	"""function (source) {
			if (source.activeMoveActions > 1) {
				this.hint("Mat Block only works on your first turn out.");
				return false;
			}
			return !!this.queue.willAct();
		}
	""" 
	pass