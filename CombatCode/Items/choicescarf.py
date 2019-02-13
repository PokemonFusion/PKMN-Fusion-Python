def onStart(datadic : dict):
	"""function (pokemon) {
			if (pokemon.volatiles['choicelock']) {
				this.debug('removing choicelock: ' + pokemon.volatiles.choicelock);
			}
			pokemon.removeVolatile('choicelock');
		}
	""" 
	pass

def onModifyMove(datadic : dict):
	"""function (move, pokemon) {
			pokemon.addVolatile('choicelock');
		}
	""" 
	pass

def onModifySpe(datadic : dict):
	"""function (spe) {
			return this.chainModify(1.5);
		}
	""" 
	pass
