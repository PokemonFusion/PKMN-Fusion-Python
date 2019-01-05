def onSwitchIn (pokemon):
	"""function (pokemon) {
			if (pokemon.isActive && pokemon.baseTemplate.species === 'Groudon') {
				this.insertQueue({pokemon: pokemon, choice: 'runPrimal'});
			}
		}
	""" 
	pass

def onPrimal (pokemon):
	"""function (pokemon) {
			pokemon.formeChange('Groudon-Primal', this.effect, True);
		}
	""" 
	pass

def onTakeItem (item, source):
	"""function (item, source) {
			if (source.baseTemplate.baseSpecies === 'Groudon') return False;
			return True;
		}
	""" 
	pass