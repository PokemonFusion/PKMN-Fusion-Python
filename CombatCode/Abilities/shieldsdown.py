def onStart(**bvalues):
	"""function (pokemon) {
			if (pokemon.baseTemplate.baseSpecies !== 'Minior' || pokemon.transformed) return;
			if (pokemon.hp > pokemon.maxhp / 2) {
				if (pokemon.template.speciesid === 'minior') {
					pokemon.formeChange('Minior-Meteor');
				}
			} else {
				if (pokemon.template.speciesid !== 'minior') {
					pokemon.formeChange(pokemon.set.species);
				}
			}
		}
	""" 
	pass

def onResidual(**bvalues):
	"""function (pokemon) {
			if (pokemon.baseTemplate.baseSpecies !== 'Minior' || pokemon.transformed || !pokemon.hp) return;
			if (pokemon.hp > pokemon.maxhp / 2) {
				if (pokemon.template.speciesid === 'minior') {
					pokemon.formeChange('Minior-Meteor');
				}
			} else {
				if (pokemon.template.speciesid !== 'minior') {
					pokemon.formeChange(pokemon.set.species);
				}
			}
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			if (target.template.speciesid !== 'miniormeteor' || target.transformed) return;
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Shields Down');
			return false;
		}
	""" 
	pass

def onTryAddVolatile(**bvalues):
	"""function (status, target) {
			if (target.template.speciesid !== 'miniormeteor' || target.transformed) return;
			if (status.id !== 'yawn') return;
			this.add('-immune', target, '[from] ability: Shields Down');
			return null;
		}
	""" 
	pass
