def onTryHit(datadic : dict):
	"""function (pokemon) {
			return !!this.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target) {
				this.add('-singleturn', target, 'Protect');
			}
	""" 
	pass

def onTryHit(datadic : dict):
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

def onHit(datadic : dict):
	"""function (target, source, move) {
				if (move.isZPowered && move.flags['contact']) {
					this.boost({atk: -2}, source, target, this.getMove("King's Shield"));
				}
			}
	""" 
	pass
