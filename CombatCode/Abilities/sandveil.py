def onImmunity(**bvalues):
	"""function (type, pokemon) {
			if (type === 'sandstorm')
				return False;
		}
	""" 
	pass

def onModifyAccuracy(**bvalues):
	"""function (accuracy) {
			if (typeof accuracy !== 'number')
				return;
			if (this.field.isWeather('sandstorm')) {
				this.debug('Sand Veil - decreasing accuracy');
				return this.chainModify([3277, 4096]);
			}
		}
	""" 
	pass
