def onHit(**bvalues):
	"""function (pokemon) {
			var oldAbility = pokemon.setAbility('insomnia');
			if (oldAbility) {
				this.add('-ability', pokemon, 'Insomnia', '[from] move: Worry Seed');
				if (pokemon.status === 'slp') {
					pokemon.cureStatus();
				}
				return;
			}
			return false;
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

def onTryImmunity(**bvalues):
	"""function (target) {
			// Truant and Insomnia have special treatment; they fail before
			// checking accuracy and will double Stomping Tantrum's BP
			if (target.ability === 'truant' || target.ability === 'insomnia') {
				return false;
			}
		}
	""" 
	pass
