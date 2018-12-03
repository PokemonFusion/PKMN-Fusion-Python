def basePowerCallback (pokemon):
	"""function (pokemon) {
			if (!pokemon.volatiles['stockpile'] || !pokemon.volatiles['stockpile'].layers) return false;
			return pokemon.volatiles['stockpile'].layers * 100;
		}
	""" 
	pass

def onTry (pokemon):
	"""function (pokemon) {
			if (!pokemon.volatiles['stockpile']) {
				return false;
			}
		}
	""" 
	pass

def onAfterMove (pokemon):
	"""function (pokemon) {
			pokemon.removeVolatile('stockpile');
		}
	""" 
	pass