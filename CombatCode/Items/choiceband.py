def onModifyAtk(**bvalues):
	"""function (atk, pokemon) {
			if (pokemon.volatiles['dynamax'])
				return;
			return this.chainModify(1.5);
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, pokemon) {
			pokemon.addVolatile('choicelock');
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
