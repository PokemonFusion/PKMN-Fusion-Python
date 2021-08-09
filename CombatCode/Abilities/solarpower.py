def onModifySpA(**bvalues):
	"""function (spa, pokemon) {
			if (['sunnyday', 'desolateland'].includes(pokemon.effectiveWeather())) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass

def onWeather(**bvalues):
	"""function (target, source, effect) {
			if (target.hasItem('utilityumbrella'))
				return;
			if (effect.id === 'sunnyday' || effect.id === 'desolateland') {
				this.damage(target.baseMaxhp / 8, target, target);
			}
		}
	""" 
	pass
