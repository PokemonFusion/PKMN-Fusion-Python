def onPrepareHit(**bvalues):
	"""function (pokemon) {
			return !!this.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-singleturn', target, 'Protect');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				if (!move.flags['protect']) {
					if (move.isZ) move.zBrokeProtect = true;
					return;
				}
				this.add('-activate', target, 'move: Protect');
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
