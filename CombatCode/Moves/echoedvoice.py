def basePowerCallback ():
	"""function () {
			if (this.pseudoWeather.echoedvoice) {
				return 40 * this.pseudoWeather.echoedvoice.multiplier;
			}
			return 40;
		}
	""" 
	pass

def onTry ():
	"""function () {
			this.addPseudoWeather('echoedvoice');
		}
	""" 
	pass

def onStart ():
	"""function () {
				this.effectData.multiplier = 1;
			}
	""" 
	pass

def onRestart ():
	"""function () {
				if (this.effectData.duration !== 2) {
					this.effectData.duration = 2;
					if (this.effectData.multiplier < 5) {
						this.effectData.multiplier++;
					}
				}
			}
	""" 
	pass