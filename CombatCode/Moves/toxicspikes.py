def onStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'move: Toxic Spikes');
				this.effectData.layers = 1;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (side) {
				if (this.effectData.layers >= 2) return false;
				this.add('-sidestart', side, 'move: Toxic Spikes');
				this.effectData.layers++;
			}
	""" 
	pass

def onSwitchIn(**bvalues):
	"""function (pokemon) {
				if (!pokemon.isGrounded()) return;
				if (!pokemon.runImmunity('Poison')) return;
				if (pokemon.hasType('Poison')) {
					this.add('-sideend', pokemon.side, 'move: Toxic Spikes', '[of] ' + pokemon);
					pokemon.side.removeSideCondition('toxicspikes');
				} else if (this.effectData.layers >= 2) {
					pokemon.trySetStatus('tox', pokemon.side.foe.active[0]);
				} else {
					pokemon.trySetStatus('psn', pokemon.side.foe.active[0]);
				}
			}
	""" 
	pass
