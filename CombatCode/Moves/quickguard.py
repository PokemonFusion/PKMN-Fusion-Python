def onTryHitSide(**bvalues):
	"""function (side, source) {
			return this.willAct();
		}
	""" 
	pass

def onHitSide(**bvalues):
	"""function (side, source) {
			source.addVolatile('stall');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source) {
				this.add('-singleturn', source, 'Quick Guard');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				// Quick Guard blocks moves with positive priority, even those given increased priority by Prankster or Gale Wings.
				// (e.g. it blocks 0 priority moves boosted by Prankster or Gale Wings; Quick Claw/Custap Berry do not count)
				if (move.priority <= 0.1) return;
				if (!move.flags['protect']) {
					if (move.isZ) move.zBrokeProtect = true;
					return;
				}
				this.add('-activate', target, 'move: Quick Guard');
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
