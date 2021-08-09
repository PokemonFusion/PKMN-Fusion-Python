def onStart (target):
	"""function (target) {
				this.add('-singleturn', target, 'Protect');
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
				if (move.smartTarget) {
					move.smartTarget = false;
				}
				else {
					this.add('-activate', target, 'move: Protect');
				}
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

def onHit (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onPrepareHit (pokemon):
	"""function (pokemon) {
			return !!this.queue.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass