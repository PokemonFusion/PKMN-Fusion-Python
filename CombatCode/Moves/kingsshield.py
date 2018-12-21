def onTryHit (pokemon):
	"""function (pokemon) {
			return !!this.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass

def onHit (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
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
					this.boost({atk: -2}, source, target, this.getMove("King's Shield"));
				}
				return null;
			}
	""" 
	pass

def onHit (target, source, move):
	"""function (target, source, move) {
				if (move.isZPowered && move.flags['contact']) {
					this.boost({atk: -2}, source, target, this.getMove("King's Shield"));
				}
			}
	""" 
	pass