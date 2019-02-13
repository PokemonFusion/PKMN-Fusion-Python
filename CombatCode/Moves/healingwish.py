def onTryHit(datadic : dict):
	"""function (pokemon, target, move) {
			if (!this.canSwitch(pokemon.side)) {
				delete move.selfdestruct;
				return false;
			}
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (side, source) {
				this.debug('Healing Wish started on ' + side.name);
				this.effectData.positions = [];
				for (let i = 0; i < side.active.length; i++) {
					this.effectData.positions[i] = false;
				}
				this.effectData.positions[source.position] = true;
			}
	""" 
	pass

def onRestart(datadic : dict):
	"""function (side, source) {
				this.effectData.positions[source.position] = true;
			}
	""" 
	pass

def onSwitchIn(datadic : dict):
	"""function (target) {
				const positions = /**@type {boolean[]} */ (this.effectData.positions);
				if (!positions[target.position]) {
					return;
				}
				if (!target.fainted) {
					target.heal(target.maxhp);
					target.setStatus('');
					this.add('-heal', target, target.getHealth, '[from] move: Healing Wish');
					positions[target.position] = false;
				}
				if (!positions.some(affected => affected === true)) {
					target.side.removeSideCondition('healingwish');
				}
			}
	""" 
	pass
