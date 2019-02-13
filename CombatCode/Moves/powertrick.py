def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-start', pokemon, 'Power Trick');
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onCopy(datadic : dict):
	"""function (pokemon) {
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Power Trick');
				let newatk = pokemon.stats.def;
				let newdef = pokemon.stats.atk;
				pokemon.stats.atk = newatk;
				pokemon.stats.def = newdef;
			}
	""" 
	pass

def onRestart(datadic : dict):
	"""function (pokemon) {
				pokemon.removeVolatile('Power Trick');
			}
	""" 
	pass
