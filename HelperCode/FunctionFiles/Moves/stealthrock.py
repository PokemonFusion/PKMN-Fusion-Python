def onStart (side):
	"""function (side) {
				this.add('-sidestart', side, 'move: Stealth Rock');
			}
	""" 
	pass

def onSwitchIn (pokemon):
	"""function (pokemon) {
				let typeMod = this.clampIntRange(pokemon.runEffectiveness('Rock'), -6, 6);
				this.damage(pokemon.maxhp * Math.pow(2, typeMod) / 8);
			}
	""" 
	pass