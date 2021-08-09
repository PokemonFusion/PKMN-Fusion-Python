def onSideRestart(**bvalues):
	"""function (side) {
				if (this.effectState.layers >= 2)
					return false;
				this.add('-sidestart', side, 'move: Toxic Spikes');
				this.effectState.layers++;
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'move: Toxic Spikes');
				this.effectState.layers = 1;
			}
	""" 
	pass

def onSwitchIn(**bvalues):
	"""function (pokemon) {
				if (!pokemon.isGrounded())
					return;
				if (pokemon.hasType('Poison')) {
					this.add('-sideend', pokemon.side, 'move: Toxic Spikes', '[of] ' + pokemon);
					pokemon.side.removeSideCondition('toxicspikes');
				}
				else if (pokemon.hasType('Steel') || pokemon.hasItem('heavydutyboots')) {
					return;
				}
				else if (this.effectState.layers >= 2) {
					pokemon.trySetStatus('tox', pokemon.side.foe.active[0]);
				}
				else {
					pokemon.trySetStatus('psn', pokemon.side.foe.active[0]);
				}
			}
	""" 
	pass
