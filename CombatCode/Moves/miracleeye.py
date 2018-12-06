def onTryHit (target):
	"""function (target) {
			if (target.volatiles['foresight']) return false;
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Miracle Eye');
			}
	""" 
	pass

def onNegateImmunity (pokemon, type):
	"""function (pokemon, type) {
				if (pokemon.hasType('Dark') && type === 'Psychic') return false;
			}
	""" 
	pass

def onModifyBoost (boosts):
	"""function (boosts) {
				if (boosts.evasion && boosts.evasion > 0) {
					boosts.evasion = 0;
				}
			}
	""" 
	pass