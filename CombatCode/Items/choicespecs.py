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

def onModifySpA(datadic : dict):
	"""function (spa) {
			return this.chainModify(1.5);
		}
	""" 
	pass
