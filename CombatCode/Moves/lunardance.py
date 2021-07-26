def onTryHit(**bvalues):
	"""function (pokemon, target, move) {
			if (!this.canSwitch(pokemon.side)) {
				delete move.selfdestruct;
				return false;
			}
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (side, source) {
				this.debug('Lunar Dance started on ' + side.name);
				this.effectData.positions = [];
				for (const i of side.active.keys()) {
					this.effectData.positions[i] = false;
				}
				this.effectData.positions[source.position] = true;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (side, source) {
				this.effectData.positions[source.position] = true;
			}
	""" 
	pass

def onSwitchIn(**bvalues):
	"""function (target) {
				const positions = /**@type {boolean[]} */ (this.effectData.positions);
				if (target.position !== this.effectData.sourcePosition) {
					return;
				}
				if (!target.fainted) {
					target.heal(target.maxhp);
					target.setStatus('');
					for (const moveSlot of target.moveSlots) {
						moveSlot.pp = moveSlot.maxpp;
					}
					this.add('-heal', target, target.getHealth, '[from] move: Lunar Dance');
					positions[target.position] = false;
				}
				if (!positions.some(affected => affected === true)) {
					target.side.removeSideCondition('lunardance');
				}
			}
	""" 
	pass
