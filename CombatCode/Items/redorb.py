def onSwitchIn(**bvalues):
	"""function (pokemon) {
			if (pokemon.isActive && pokemon.baseTemplate.species === 'Groudon') {
				this.insertQueue({pokemon: pokemon, choice: 'runPrimal'});
			}
		}
	""" 
	pass

def onPrimal(**bvalues):
	"""function (pokemon) {
			pokemon.formeChange('Groudon-Primal', this.effect, True);
		}
	""" 
	pass

def onTakeItem(**bvalues):
	"""function (item, source) {
			if (source.baseTemplate.baseSpecies === 'Groudon') return False;
			return True;
		}
	""" 
	pass
