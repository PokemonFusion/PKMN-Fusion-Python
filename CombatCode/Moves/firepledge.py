def basePowerCallback(**bvalues):
	"""function (target, source, move) {
			if (['grasspledge', 'waterpledge'].includes(move.sourceEffect)) {
				this.add('-combine');
				return 150;
			}
			return 80;
		}
	""" 
	pass

def onPrepareHit(**bvalues):
	"""function (target, source, move) {
			for (const action of this.queue) {
				// @ts-ignore
				if (!action.move || !action.pokemon || !action.pokemon.isActive || action.pokemon.fainted) continue;
				// @ts-ignore
				if (action.pokemon.side === source.side && ['grasspledge', 'waterpledge'].includes(action.move.id)) {
					// @ts-ignore
					this.prioritizeAction(action);
					this.add('-waiting', source, action.pokemon);
					return null;
				}
			}
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move) {
			if (move.sourceEffect === 'waterpledge') {
				move.type = 'Water';
				move.forceSTAB = true;
			}
			if (move.sourceEffect === 'grasspledge') {
				move.type = 'Fire';
				move.forceSTAB = true;
			}
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
			if (move.sourceEffect === 'grasspledge') {
				target.side.addSideCondition('firepledge');
			}
			if (move.sourceEffect === 'waterpledge') {
				source.side.addSideCondition('waterpledge');
			}
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (targetSide) {
				this.add('-sidestart', targetSide, 'Fire Pledge');
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (targetSide) {
				this.add('-sideend', targetSide, 'Fire Pledge');
			}
	""" 
	pass

def onResidual(**bvalues):
	"""function (side) {
				for (const pokemon of side.active) {
					if (pokemon && !pokemon.hasType('Fire')) {
						this.damage(pokemon.maxhp / 8, pokemon);
					}
				}
			}
	""" 
	pass
