def onSideStart (target, source):
	"""function (target, source) {
				this.add('-singleturn', source, 'Wide Guard');
			}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
				// Wide Guard blocks all spread moves
				if ((move === null || move === void 0 ? void 0 : move.target) !== 'allAdjacent' && move.target !== 'allAdjacentFoes') {
					return;
				}
				if (move.isZ || move.isMax) {
					if (['gmaxoneblow', 'gmaxrapidflow'].includes(move.id))
						return;
					target.getMoveHitData(move).zBrokeProtect = true;
					return;
				}
				this.add('-activate', target, 'move: Wide Guard');
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

def onHitSide (side, source):
	"""function (side, source) {
			source.addVolatile('stall');
		}
	""" 
	pass

def onTry ():
	"""function () {
			return !!this.queue.willAct();
		}
	""" 
	pass