def basePowerCallback ():
	"""function () {
			if (this.field.pseudoWeather.echoedvoice) {
				return 40 * this.field.pseudoWeather.echoedvoice.multiplier;
			}
			return 40;
		}
	""" 
	pass

def onFieldRestart ():
	"""function () {
				if (this.effectState.duration !== 2) {
					this.effectState.duration = 2;
					if (this.effectState.multiplier < 5) {
						this.effectState.multiplier++;
					}
				}
			}
	""" 
	pass

def onFieldStart ():
	"""function () {
				this.effectState.multiplier = 1;
			}
	""" 
	pass

def onTry ():
	"""function () {
			this.field.addPseudoWeather('echoedvoice');
		}
	""" 
	pass