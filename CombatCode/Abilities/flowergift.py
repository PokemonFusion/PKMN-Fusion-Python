def onStart(**bvalues):
	"""function (pokemon) {
			delete this.effectState.forme;
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (!pokemon.isActive || pokemon.baseSpecies.baseSpecies !== 'Cherrim' || pokemon.transformed)
				return;
			if (!pokemon.hp)
				return;
			if (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {
				if (pokemon.species.id !== 'cherrimsunshine') {
					pokemon.formeChange('Cherrim-Sunshine', this.effect, False, '[msg]');
				}
			}
			else {
				if (pokemon.species.id === 'cherrimsunshine') {
					pokemon.formeChange('Cherrim', this.effect, False, '[msg]');
				}
			}
		}
	""" 
	pass

def onAllyModifyAtk(**bvalues):
	"""function (atk, pokemon) {
			if (this.effectState.target.baseSpecies.baseSpecies !== 'Cherrim')
				return;
			if (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass

def onAllyModifySpD(**bvalues):
	"""function (spd, pokemon) {
			if (this.effectState.target.baseSpecies.baseSpecies !== 'Cherrim')
				return;
			if (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass
