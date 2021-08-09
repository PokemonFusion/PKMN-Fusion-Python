def onSideStart(**bvalues):
	"""function (target, source) {
				this.add('-singleturn', source, 'Quick Guard');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				// Quick Guard blocks moves with positive priority, even those given increased priority by Prankster or Gale Wings.
				// (e.g. it blocks 0 priority moves boosted by Prankster or Gale Wings; Quick Claw/Custap Berry do not count)
				if (move.priority <= 0.1)
					return;
				if (!move.flags['protect']) {
					if (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))
						return;
					if (move.isZ || move.isMax)
						target.getMoveHitData(move).zBrokeProtect = true;
					return;
				}
				this.add('-activate', target, 'move: Quick Guard');
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

def onHitSide(**bvalues):
	"""function (side, source) {
			source.addVolatile('stall');
		}
	""" 
	pass

def onTry(**bvalues):
	"""function () {
			return !!this.queue.willAct();
		}
	""" 
	pass
