def onSideStart (side):
	"""function (side) {
				this.add('-sidestart', side, 'move: Stealth Rock');
			}
	""" 
	pass

def onSwitchIn (pokemon):
	"""function (pokemon) {
				if (pokemon.hasItem('heavydutyboots'))
					return;
				var typeMod = this.clampIntRange(pokemon.runEffectiveness(this.dex.getActiveMove('stealthrock')), -6, 6);
				this.damage(pokemon.maxhp * Math.pow(2, typeMod) / 8);
			}
	""" 
	pass