def onSwitchIn (pokemon):
	"""function (pokemon) {
			if (pokemon.isActive && pokemon.baseTemplate.species === 'Kyogre') {
				this.insertQueue({pokemon: pokemon, choice: 'runPrimal'});
			}
		}
	""" 
	pass

def onPrimal (pokemon):
	"""function (pokemon) {
			pokemon.formeChange('Kyogre-Primal', this.effect, True);
		}
	""" 
	pass

def onTakeItem (item, source):
	"""function (item, source) {
			if (source.baseTemplate.baseSpecies === 'Kyogre') return False;
			return True;
		}
	""" 
	pass