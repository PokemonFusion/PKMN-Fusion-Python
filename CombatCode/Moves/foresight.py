def onTryHit(datadic : dict):
	"""function (target) {
			if (target.volatiles['miracleeye']) return false;
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Foresight');
			}
	""" 
	pass

def onNegateImmunity(datadic : dict):
	"""function (pokemon, type) {
				if (pokemon.hasType('Ghost') && ['Normal', 'Fighting'].includes(type)) return false;
			}
	""" 
	pass

def onModifyBoost(datadic : dict):
	"""function (boosts) {
				if (boosts.evasion && boosts.evasion > 0) {
					boosts.evasion = 0;
				}
			}
	""" 
	pass
