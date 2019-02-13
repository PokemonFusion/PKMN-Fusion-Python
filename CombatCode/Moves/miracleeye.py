def onTryHit(datadic : dict):
	"""function (target) {
			if (target.volatiles['foresight']) return false;
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Miracle Eye');
			}
	""" 
	pass

def onNegateImmunity(datadic : dict):
	"""function (pokemon, type) {
				if (pokemon.hasType('Dark') && type === 'Psychic') return false;
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
