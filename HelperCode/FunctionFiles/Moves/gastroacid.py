def onCopy (pokemon):
	"""function (pokemon) {
				if (pokemon.getAbility().isPermanent)
					pokemon.removeVolatile('gastroacid');
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-endability', pokemon);
				this.singleEvent('End', pokemon.getAbility(), pokemon.abilityState, pokemon, pokemon, 'gastroacid');
			}
	""" 
	pass

def onTryHit (target):
	"""function (target) {
			if (target.getAbility().isPermanent) {
				return false;
			}
		}
	""" 
	pass