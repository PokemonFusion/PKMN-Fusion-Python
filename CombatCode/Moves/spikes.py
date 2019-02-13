def onStart(datadic : dict):
	"""function (side) {
				this.add('-sidestart', side, 'Spikes');
				this.effectData.layers = 1;
			}
	""" 
	pass

def onRestart(datadic : dict):
	"""function (side) {
				if (this.effectData.layers >= 3) return false;
				this.add('-sidestart', side, 'Spikes');
				this.effectData.layers++;
			}
	""" 
	pass

def onSwitchIn(datadic : dict):
	"""function (pokemon) {
				if (!pokemon.isGrounded()) return;
				let damageAmounts = [0, 3, 4, 6]; // 1/8, 1/6, 1/4
				this.damage(damageAmounts[this.effectData.layers] * pokemon.maxhp / 24);
			}
	""" 
	pass
