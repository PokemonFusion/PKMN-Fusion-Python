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
				this.add('-singleturn', source, 'Wide Guard');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				// Wide Guard blocks all spread moves
				if (move && move.target !== 'allAdjacent' && move.target !== 'allAdjacentFoes') {
					return;
				}
				if (move.isZ) {
					move.zBrokeProtect = true;
					return;
				}
				this.add('-activate', target, 'move: Wide Guard');
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
