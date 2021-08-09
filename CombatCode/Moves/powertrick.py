def onCopy(**bvalues):
	"""function (pokemon) {
				var newatk = pokemon.storedStats.def;
				var newdef = pokemon.storedStats.atk;
				pokemon.storedStats.atk = newatk;
				pokemon.storedStats.def = newdef;
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Power Trick');
				var newatk = pokemon.storedStats.def;
				var newdef = pokemon.storedStats.atk;
				pokemon.storedStats.atk = newatk;
				pokemon.storedStats.def = newdef;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (pokemon) {
				pokemon.removeVolatile('Power Trick');
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Power Trick');
				var newatk = pokemon.storedStats.def;
				var newdef = pokemon.storedStats.atk;
				pokemon.storedStats.atk = newatk;
				pokemon.storedStats.def = newdef;
			}
	""" 
	pass
