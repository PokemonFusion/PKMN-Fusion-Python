def basePowerCallback (target, source, move):
	"""function (target, source, move) {
			if (['firepledge', 'grasspledge'].includes(move.sourceEffect)) {
				this.add('-combine');
				return 150;
			}
			return 80;
		}
	""" 
	pass

def onPrepareHit (target, source, move):
	"""function (target, source, move) {
			for (const action of this.queue) {
				// @ts-ignore
				if (!action.move || !action.pokemon || !action.pokemon.isActive || action.pokemon.fainted) continue;
				// @ts-ignore
				if (action.pokemon.side === source.side && ['firepledge', 'grasspledge'].includes(action.move.id)) {
					// @ts-ignore
					this.prioritizeAction(action);
					this.add('-waiting', source, action.pokemon);
					return null;
				}
			}
		}
	""" 
	pass

def onModifyMove (move):
	"""function (move) {
			if (move.sourceEffect === 'grasspledge') {
				move.type = 'Grass';
				move.forceSTAB = true;
			}
			if (move.sourceEffect === 'firepledge') {
				move.type = 'Water';
				move.forceSTAB = true;
			}
		}
	""" 
	pass

def onHit (target, source, move):
	"""function (target, source, move) {
			if (move.sourceEffect === 'firepledge') {
				source.side.addSideCondition('waterpledge');
			}
			if (move.sourceEffect === 'grasspledge') {
				target.side.addSideCondition('grasspledge');
			}
		}
	""" 
	pass

def onStart (targetSide):
	"""function (targetSide) {
				this.add('-sidestart', targetSide, 'Water Pledge');
			}
	""" 
	pass

def onEnd (targetSide):
	"""function (targetSide) {
				this.add('-sideend', targetSide, 'Water Pledge');
			}
	""" 
	pass

def onModifyMove (move):
	"""function (move) {
				if (move.secondaries && move.id !== 'secretpower') {
					this.debug('doubling secondary chance');
					for (const secondary of move.secondaries) {
						if (secondary.chance) secondary.chance *= 2;
					}
				}
			}
	""" 
	pass