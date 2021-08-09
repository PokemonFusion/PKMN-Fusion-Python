def onModifyBoost(**bvalues):
	"""function (boosts) {
				if (boosts.evasion && boosts.evasion > 0) {
					boosts.evasion = 0;
				}
			}
	""" 
	pass

def onNegateImmunity(**bvalues):
	"""function (pokemon, type) {
				if (pokemon.hasType('Dark') && type === 'Psychic')
					return false;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Miracle Eye');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (target.volatiles['foresight'])
				return false;
		}
	""" 
	pass
