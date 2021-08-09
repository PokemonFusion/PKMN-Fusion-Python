def onImmunity (type, pokemon):
	"""function (type, pokemon) {
			if (type === 'hail')
				return False;
		}
	""" 
	pass

def onModifyAccuracy (accuracy):
	"""function (accuracy) {
			if (typeof accuracy !== 'number')
				return;
			if (this.field.isWeather('hail')) {
				this.debug('Snow Cloak - decreasing accuracy');
				return this.chainModify([3277, 4096]);
			}
		}
	""" 
	pass