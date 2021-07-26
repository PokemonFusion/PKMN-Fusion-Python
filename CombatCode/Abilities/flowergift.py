def onStart(**bvalues):
	"""function (pokemon) {
			delete this.effectData.forme;
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (!pokemon.isActive || pokemon.baseTemplate.baseSpecies !== 'Cherrim' || pokemon.transformed) return;
			if (this.isWeather(['sunnyday', 'desolateland'])) {
				if (pokemon.template.speciesid !== 'cherrimsunshine') {
					pokemon.formeChange('Cherrim-Sunshine', this.effect, false, '[msg]');
				}
			} else {
				if (pokemon.template.speciesid === 'cherrimsunshine') {
					pokemon.formeChange('Cherrim', this.effect, false, '[msg]');
				}
			}
		}
	""" 
	pass

def onAllyModifyAtk(**bvalues):
	"""function (atk) {
			if (this.effectData.target.baseTemplate.baseSpecies !== 'Cherrim') return;
			if (this.isWeather(['sunnyday', 'desolateland'])) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass

def onAllyModifySpD(**bvalues):
	"""function (spd) {
			if (this.effectData.target.baseTemplate.baseSpecies !== 'Cherrim') return;
			if (this.isWeather(['sunnyday', 'desolateland'])) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass
