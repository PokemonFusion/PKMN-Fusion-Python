def basePowerCallback(**bvalues):
	"""function (pokemon) {
			if (!pokemon.volatiles['stockpile'] || !pokemon.volatiles['stockpile'].layers) return false;
			return pokemon.volatiles['stockpile'].layers * 100;
		}
	""" 
	pass

def onTry(**bvalues):
	"""function (pokemon) {
			if (!pokemon.volatiles['stockpile']) {
				return false;
			}
		}
	""" 
	pass

def onAfterMove(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('stockpile');
		}
	""" 
	pass
