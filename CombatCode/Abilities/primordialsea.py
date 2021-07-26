def onStart(**bvalues):
	"""function (source) {
			this.setWeather('primordialsea');
		}
	""" 
	pass

def onAnySetWeather(**bvalues):
	"""function (target, source, weather) {
			if (this.getWeather().id === 'primordialsea' && !['desolateland', 'primordialsea', 'deltastream'].includes(weather.id)) return false;
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			if (this.weatherData.source !== pokemon) return;
			for (const side of this.sides) {
				for (const target of side.active) {
					if (target === pokemon) continue;
					if (target && target.hp && target.hasAbility('primordialsea')) {
						this.weatherData.source = target;
						return;
					}
				}
			}
			this.clearWeather();
		}
	""" 
	pass
