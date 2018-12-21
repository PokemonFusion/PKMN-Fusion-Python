def onStart (pokemon):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Power Trick');
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onCopy (pokemon):
	"""function (pokemon) {
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Power Trick');
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onRestart (pokemon):
	"""function (pokemon) {
				pokemon.removeVolatile('Power Trick');
			}
	""" 
	pass