def onModifyBoost (boosts):
	"""function (boosts) {
				if (boosts.evasion && boosts.evasion > 0) {
					boosts.evasion = 0;
				}
			}
	""" 
	pass

def onNegateImmunity (pokemon, type):
	"""function (pokemon, type) {
				if (pokemon.hasType('Ghost') && ['Normal', 'Fighting'].includes(type))
					return false;
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Foresight');
			}
	""" 
	pass

def onTryHit (target):
	"""function (target) {
			if (target.volatiles['miracleeye'])
				return false;
		}
	""" 
	pass