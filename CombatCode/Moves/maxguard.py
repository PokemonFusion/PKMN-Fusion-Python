def onStart(**bvalues):
	"""function (target) {
				this.add('-singleturn', target, 'Max Guard');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				if (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))
					return;
				/** moves blocked by Max Guard but not Protect */
				var overrideBypassProtect = [
					'block', 'flowershield', 'gearup', 'magneticflux', 'phantomforce', 'psychup', 'shadowforce', 'teatime', 'transform',
				];
				var blockedByMaxGuard = (this.dex.moves.get(move.id).flags['protect'] ||
					move.isZ || move.isMax || overrideBypassProtect.includes(move.id));
				if (!blockedByMaxGuard) {
					return;
				}
				if (move.smartTarget) {
					move.smartTarget = false;
				}
				else {
					this.add('-activate', target, 'move: Max Guard');
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
