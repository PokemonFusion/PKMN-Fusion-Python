def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.baseSpecies.baseSpecies !== 'Castform' || pokemon.transformed)
				return;
			var forme = null;
			switch (pokemon.effectiveWeather()) {
				case 'sunnyday':
				case 'desolateland':
					if (pokemon.species.id !== 'castformsunny')
						forme = 'Castform-Sunny';
					break;
				case 'raindance':
				case 'primordialsea':
					if (pokemon.species.id !== 'castformrainy')
						forme = 'Castform-Rainy';
					break;
				case 'hail':
					if (pokemon.species.id !== 'castformsnowy')
						forme = 'Castform-Snowy';
					break;
				default:
					if (pokemon.species.id !== 'castform')
						forme = 'Castform';
					break;
			}
			if (pokemon.isActive && forme) {
				pokemon.formeChange(forme, this.effect, False, '[msg]');
			}
		}
	""" 
	pass
