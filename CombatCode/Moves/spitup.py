def basePowerCallback(datadic : dict):
	"""function (pokemon) {
			if (!pokemon.volatiles['stockpile'] || !pokemon.volatiles['stockpile'].layers) return false;
			return pokemon.volatiles['stockpile'].layers * 100;
		}
	""" 
	pass

def onTry(datadic : dict):
	"""function (pokemon) {
			if (!pokemon.volatiles['stockpile']) {
				return false;
			}
		}
	""" 
	pass

def onAfterMove(datadic : dict):
	"""function (pokemon) {
			pokemon.removeVolatile('stockpile');
		}
	""" 
	pass
