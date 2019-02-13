def basePowerCallback(datadic : dict):
	"""function (target, source, move) {
			if (['waterpledge', 'firepledge'].includes(move.sourceEffect)) {
				this.add('-combine');
				return 150;
			}
			return 80;
		}
	""" 
	pass

def onPrepareHit(datadic : dict):
	"""function (target, source, move) {
			for (const action of this.queue) {
				// @ts-ignore
				if (!action.move || !action.pokemon || !action.pokemon.isActive || action.pokemon.fainted) continue;
				// @ts-ignore
				if (action.pokemon.side === source.side && ['waterpledge', 'firepledge'].includes(action.move.id)) {
					// @ts-ignore
					this.prioritizeAction(action);
					this.add('-waiting', source, action.pokemon);
					return null;
				}
			}
		}
	""" 
	pass

def onModifyMove(datadic : dict):
	"""function (move) {
			if (move.sourceEffect === 'waterpledge') {
				move.type = 'Grass';
				move.forceSTAB = true;
			}
			if (move.sourceEffect === 'firepledge') {
				move.type = 'Fire';
				move.forceSTAB = true;
			}
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (target, source, move) {
			if (move.sourceEffect === 'waterpledge') {
				target.side.addSideCondition('grasspledge');
			}
			if (move.sourceEffect === 'firepledge') {
				target.side.addSideCondition('firepledge');
			}
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (targetSide) {
				this.add('-sidestart', targetSide, 'Grass Pledge');
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (targetSide) {
				this.add('-sideend', targetSide, 'Grass Pledge');
			}
	""" 
	pass

def onModifySpe(datadic : dict):
	"""function (spe, pokemon) {
				return this.chainModify(0.25);
			}
	""" 
	pass
