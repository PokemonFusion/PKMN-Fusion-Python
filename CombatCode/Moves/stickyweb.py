def onStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'move: Sticky Web');
			}
	""" 
	pass

def onSwitchIn(**bvalues):
	"""function (pokemon) {
				if (!pokemon.isGrounded()) return;
				this.add('-activate', pokemon, 'move: Sticky Web');
				this.boost({spe: -1}, pokemon, pokemon.side.foe.active[0], this.getMove('stickyweb'));
			}
	""" 
	pass
