def onHit (target, source, move):
	"""function (target, source, move) {
				if (move.isZOrMaxPowered && this.checkMoveMakesContact(move, source, target)) {
					this.boost({ atk: -1 }, source, target, this.dex.getActiveMove("King's Shield"));
				}
			}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-singleturn', target, 'Protect');
			}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
				if (!move.flags['protect'] || move.category === 'Status') {
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
				if (this.checkMoveMakesContact(move, source, target)) {
					this.boost({ atk: -1 }, source, target, this.dex.getActiveMove("King's Shield"));
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