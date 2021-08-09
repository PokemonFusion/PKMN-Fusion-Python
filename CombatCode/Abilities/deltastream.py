def onStart(**bvalues):
	"""function (source) {
			this.field.setWeather('deltastream');
		}
	""" 
	pass

def onAnySetWeather(**bvalues):
	"""function (target, source, weather) {
			var strongWeathers = ['desolateland', 'primordialsea', 'deltastream'];
			if (this.field.getWeather().id === 'deltastream' && !strongWeathers.includes(weather.id))
				return False;
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			if (this.field.weatherState.source !== pokemon)
				return;
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var target = _a[_i];
				if (target === pokemon)
					continue;
				if (target.hasAbility('deltastream')) {
					this.field.weatherState.source = target;
					return;
				}
			}
			this.field.clearWeather();
		}
	""" 
	pass
