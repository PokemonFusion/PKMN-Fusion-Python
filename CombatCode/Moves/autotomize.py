def onTryHit(**bvalues):
	"""function (pokemon) {
			let hasContrary = pokemon.hasAbility('contrary');
			if ((!hasContrary && pokemon.boosts.spe === 6) || (hasContrary && pokemon.boosts.spe === -6)) {
				return false;
			}
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				if (pokemon.template.weightkg > 0.1) {
					this.effectData.multiplier = 1;
					this.add('-start', pokemon, 'Autotomize');
				}
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (pokemon) {
				if (pokemon.template.weightkg - (this.effectData.multiplier * 100) > 0.1) {
					this.effectData.multiplier++;
					this.add('-start', pokemon, 'Autotomize');
				}
			}
	""" 
	pass

def onModifyWeight(**bvalues):
	"""function (weight, pokemon) {
				if (this.effectData.multiplier) {
					weight -= this.effectData.multiplier * 100;
					if (weight < 0.1) weight = 0.1;
					return weight;
				}
			}
	""" 
	pass
