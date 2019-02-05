def onModifySpA(datadic : dict):
	"""function (spa, pokemon) {
			if (this.isWeather(['sunnyday', 'desolateland'])) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass

def onWeather(datadic : dict):
	"""function (target, source, effect) {
			if (effect.id === 'sunnyday' || effect.id === 'desolateland') {
				this.damage(target.maxhp / 8, target, target);
			}
		}
	""" 
	pass
