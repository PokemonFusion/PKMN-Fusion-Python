def onModifyMove(**bvalues):
	"""function (move, pokemon) {
			pokemon.addVolatile('choicelock');
		}
	""" 
	pass

def onModifySpe(**bvalues):
	"""function (spe, pokemon) {
			if (pokemon.volatiles['dynamax'])
				return;
			return this.chainModify(1.5);
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
			if (pokemon.volatiles['choicelock']) {
				this.debug('removing choicelock: ' + pokemon.volatiles['choicelock']);
			}
			pokemon.removeVolatile('choicelock');
		}
	""" 
	pass
