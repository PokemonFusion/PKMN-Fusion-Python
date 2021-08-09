def onCopy (pokemon):
	"""function (pokemon) {
				var newatk = pokemon.storedStats.def;
				var newdef = pokemon.storedStats.atk;
				pokemon.storedStats.atk = newatk;
				pokemon.storedStats.def = newdef;
			}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Power Trick');
				var newatk = pokemon.storedStats.def;
				var newdef = pokemon.storedStats.atk;
				pokemon.storedStats.atk = newatk;
				pokemon.storedStats.def = newdef;
			}
	""" 
	pass

def onRestart (pokemon):
	"""function (pokemon) {
				pokemon.removeVolatile('Power Trick');
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Power Trick');
				var newatk = pokemon.storedStats.def;
				var newdef = pokemon.storedStats.atk;
				pokemon.storedStats.atk = newatk;
				pokemon.storedStats.def = newdef;
			}
	""" 
	pass