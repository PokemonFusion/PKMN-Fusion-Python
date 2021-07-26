def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Power Trick');
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onCopy(**bvalues):
	"""function (pokemon) {
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Power Trick');
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (pokemon) {
				pokemon.removeVolatile('Power Trick');
			}
	""" 
	pass
