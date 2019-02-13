def onStart(datadic : dict):
	"""function (source) {
			this.setWeather('deltastream');
		}
	""" 
	pass

def onAnySetWeather(datadic : dict):
	"""function (target, source, weather) {
			if (this.getWeather().id === 'deltastream' && !['desolateland', 'primordialsea', 'deltastream'].includes(weather.id)) return false;
		}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
			if (this.weatherData.source !== pokemon) return;
			for (const side of this.sides) {
				for (const target of side.active) {
					if (target === pokemon) continue;
					if (target && target.hp && target.hasAbility('deltastream')) {
						this.weatherData.source = target;
						return;
					}
				}
			}
			this.clearWeather();
		}
	""" 
	pass
