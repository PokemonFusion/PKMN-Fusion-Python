def onHit(**bvalues):
	"""function (target, source, move) {
				if (move.isZOrMaxPowered && this.checkMoveMakesContact(move, source, target)) {
					this.damage(source.baseMaxhp / 8, source, target);
				}
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
					this.damage(source.baseMaxhp / 8, source, target);
				}
				return this.NOT_FAIL;
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onPrepareHit(**bvalues):
	"""function (pokemon) {
			return !!this.queue.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass
