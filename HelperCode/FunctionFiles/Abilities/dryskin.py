def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (target !== source && move.type === 'Water') {
				if (!this.heal(target.baseMaxhp / 4)) {
					this.add('-immune', target, '[from] ability: Dry Skin');
				}
				return null;
			}
		}
	""" 
	pass

def onFoeBasePower (basePower, attacker, defender, move):
	"""function (basePower, attacker, defender, move) {
			if (this.effectState.target !== defender)
				return;
			if (move.type === 'Fire') {
				return this.chainModify(1.25);
			}
		}
	""" 
	pass

def onWeather (target, source, effect):
	"""function (target, source, effect) {
			if (target.hasItem('utilityumbrella'))
				return;
			if (effect.id === 'raindance' || effect.id === 'primordialsea') {
				this.heal(target.baseMaxhp / 8);
			}
			else if (effect.id === 'sunnyday' || effect.id === 'desolateland') {
				this.damage(target.baseMaxhp / 8, target, target);
			}
		}
	""" 
	pass