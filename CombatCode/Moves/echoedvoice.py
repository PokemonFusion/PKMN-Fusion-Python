def basePowerCallback(**bvalues):
	"""function () {
			if (this.field.pseudoWeather.echoedvoice) {
				return 40 * this.field.pseudoWeather.echoedvoice.multiplier;
			}
			return 40;
		}
	""" 
	pass

def onFieldRestart(**bvalues):
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

def onFieldStart(**bvalues):
	"""function () {
				this.effectState.multiplier = 1;
			}
	""" 
	pass

def onTry(**bvalues):
	"""function () {
			this.field.addPseudoWeather('echoedvoice');
		}
	""" 
	pass
