def onPrimal(**bvalues):
	"""function (pokemon) {
			pokemon.formeChange('Groudon-Primal', this.effect, true);
		}
	""" 
	pass

def onSwitchIn(**bvalues):
	"""function (pokemon) {
			if (pokemon.isActive && pokemon.baseSpecies.name === 'Groudon') {
				this.queue.insertChoice({ choice: 'runPrimal', pokemon: pokemon });
			}
		}
	""" 
	pass

def onTakeItem(**bvalues):
	"""function (item, source) {
			if (source.baseSpecies.baseSpecies === 'Groudon')
				return false;
			return true;
		}
	""" 
	pass
