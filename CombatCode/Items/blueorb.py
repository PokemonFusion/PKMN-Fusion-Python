def onPrimal(**bvalues):
	"""function (pokemon) {
			pokemon.formeChange('Kyogre-Primal', this.effect, true);
		}
	""" 
	pass

def onSwitchIn(**bvalues):
	"""function (pokemon) {
			if (pokemon.isActive && pokemon.baseSpecies.name === 'Kyogre') {
				this.queue.insertChoice({ choice: 'runPrimal', pokemon: pokemon });
			}
		}
	""" 
	pass

def onTakeItem(**bvalues):
	"""function (item, source) {
			if (source.baseSpecies.baseSpecies === 'Kyogre')
				return false;
			return true;
		}
	""" 
	pass
