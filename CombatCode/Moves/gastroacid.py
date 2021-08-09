def onCopy(**bvalues):
	"""function (pokemon) {
				if (pokemon.getAbility().isPermanent)
					pokemon.removeVolatile('gastroacid');
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-endability', pokemon);
				this.singleEvent('End', pokemon.getAbility(), pokemon.abilityState, pokemon, pokemon, 'gastroacid');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (target.getAbility().isPermanent) {
				return false;
			}
		}
	""" 
	pass
