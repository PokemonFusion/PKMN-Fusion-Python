def onStart (pokemon):
	"""function (pokemon) {
			if (pokemon.baseSpecies.baseSpecies !== 'Minior' || pokemon.transformed)
				return;
			if (pokemon.hp > pokemon.maxhp / 2) {
				if (pokemon.species.forme !== 'Meteor') {
					pokemon.formeChange('Minior-Meteor');
				}
			}
			else {
				if (pokemon.species.forme === 'Meteor') {
					pokemon.formeChange(pokemon.set.species);
				}
			}
		}
	""" 
	pass

def onResidual (pokemon):
	"""function (pokemon) {
			if (pokemon.baseSpecies.baseSpecies !== 'Minior' || pokemon.transformed || !pokemon.hp)
				return;
			if (pokemon.hp > pokemon.maxhp / 2) {
				if (pokemon.species.forme !== 'Meteor') {
					pokemon.formeChange('Minior-Meteor');
				}
			}
			else {
				if (pokemon.species.forme === 'Meteor') {
					pokemon.formeChange(pokemon.set.species);
				}
			}
		}
	""" 
	pass

def onSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			var _a;
			if (target.species.id !== 'miniormeteor' || target.transformed)
				return;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				this.add('-immune', target, '[from] ability: Shields Down');
			}
			return False;
		}
	""" 
	pass

def onTryAddVolatile (status, target):
	"""function (status, target) {
			if (target.species.id !== 'miniormeteor' || target.transformed)
				return;
			if (status.id !== 'yawn')
				return;
			this.add('-immune', target, '[from] ability: Shields Down');
			return null;
		}
	""" 
	pass