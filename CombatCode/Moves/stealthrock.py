def onStart(datadic : dict):
	"""function (side) {
				this.add('-sidestart', side, 'move: Stealth Rock');
			}
	""" 
	pass

def onSwitchIn(datadic : dict):
	"""function (pokemon) {
				let typeMod = this.clampIntRange(pokemon.runEffectiveness('Rock'), -6, 6);
				this.damage(pokemon.maxhp * Math.pow(2, typeMod) / 8);
			}
	""" 
	pass
