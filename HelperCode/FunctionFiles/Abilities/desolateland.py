def onStart (source):
	"""function (source) {
			this.field.setWeather('desolateland');
		}
	""" 
	pass

def onAnySetWeather (target, source, weather):
	"""function (target, source, weather) {
			var strongWeathers = ['desolateland', 'primordialsea', 'deltastream'];
			if (this.field.getWeather().id === 'desolateland' && !strongWeathers.includes(weather.id))
				return False;
		}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
			if (this.field.weatherState.source !== pokemon)
				return;
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var target = _a[_i];
				if (target === pokemon)
					continue;
				if (target.hasAbility('desolateland')) {
					this.field.weatherState.source = target;
					return;
				}
			}
			this.field.clearWeather();
		}
	""" 
	pass