def onSwitchIn(**bvalues):
	"""function (pokemon) {
			if (pokemon.isActive && pokemon.baseTemplate.species === 'Kyogre') {
				this.insertQueue({pokemon: pokemon, choice: 'runPrimal'});
			}
		}
	""" 
	pass

def onPrimal(**bvalues):
	"""function (pokemon) {
			pokemon.formeChange('Kyogre-Primal', this.effect, True);
		}
	""" 
	pass

def onTakeItem(**bvalues):
	"""function (item, source) {
			if (source.baseTemplate.baseSpecies === 'Kyogre') return False;
			return True;
		}
	""" 
	pass
