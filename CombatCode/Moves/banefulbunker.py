def onTryHit(**bvalues):
	"""function (target, source, move) {
			return !!this.willAct() && this.runEvent('StallMove', target);
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
				this.add('-singleturn', target, 'move: Protect');
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
				if (move.flags['contact']) {
					source.trySetStatus('psn', target);
				}
				return null;
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
				if (move.isZPowered && move.flags['contact']) {
					source.trySetStatus('psn', target);
				}
			}
	""" 
	pass
