def basePowerCallback(**bvalues):
	"""function (pokemon) {
			var _a;
			if (!((_a = pokemon.volatiles['stockpile']) === null || _a === void 0 ? void 0 : _a.layers))
				return false;
			return pokemon.volatiles['stockpile'].layers * 100;
		}
	""" 
	pass

def onAfterMove(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('stockpile');
		}
	""" 
	pass

def onTry(**bvalues):
	"""function (source) {
			return !!source.volatiles['stockpile'];
		}
	""" 
	pass
