def onSideStart (side):
	"""function (side) {
				this.add('-sidestart', side, 'move: Sticky Web');
			}
	""" 
	pass

def onSwitchIn (pokemon):
	"""function (pokemon) {
				if (!pokemon.isGrounded())
					return;
				if (pokemon.hasItem('heavydutyboots'))
					return;
				this.add('-activate', pokemon, 'move: Sticky Web');
				this.boost({ spe: -1 }, pokemon, this.effectState.source, this.dex.getActiveMove('stickyweb'));
			}
	""" 
	pass