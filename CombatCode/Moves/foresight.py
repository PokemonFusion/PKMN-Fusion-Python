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
				if (pokemon.hasType('Ghost') && ['Normal', 'Fighting'].includes(type))
					return false;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Foresight');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (target.volatiles['miracleeye'])
				return false;
		}
	""" 
	pass
