def onSwitchIn(datadic : dict):
	"""function (pokemon) {
			if (pokemon.isActive && pokemon.baseTemplate.species === 'Groudon') {
				this.insertQueue({pokemon: pokemon, choice: 'runPrimal'});
			}
		}
	""" 
	pass

def onPrimal(datadic : dict):
	"""function (pokemon) {
			pokemon.formeChange('Groudon-Primal', this.effect, True);
		}
	""" 
	pass

def onTakeItem(datadic : dict):
	"""function (item, source) {
			if (source.baseTemplate.baseSpecies === 'Groudon') return False;
			return True;
		}
	""" 
	pass
