def onSideRestart (side):
	"""function (side) {
				if (this.effectState.layers >= 3)
					return false;
				this.add('-sidestart', side, 'Spikes');
				this.effectState.layers++;
			}
	""" 
	pass

def onSideStart (side):
	"""function (side) {
				this.add('-sidestart', side, 'Spikes');
				this.effectState.layers = 1;
			}
	""" 
	pass

def onSwitchIn (pokemon):
	"""function (pokemon) {
				if (!pokemon.isGrounded())
					return;
				if (pokemon.hasItem('heavydutyboots'))
					return;
				var damageAmounts = [0, 3, 4, 6]; // 1/8, 1/6, 1/4
				this.damage(damageAmounts[this.effectState.layers] * pokemon.maxhp / 24);
			}
	""" 
	pass