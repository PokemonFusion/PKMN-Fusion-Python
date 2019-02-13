def onAfterUseItem(datadic : dict):
	"""function (item, pokemon) {
			if (pokemon !== this.effectData.target) return;
			pokemon.addVolatile('unburden');
		}
	""" 
	pass

def onTakeItem(datadic : dict):
	"""function (item, pokemon) {
			pokemon.addVolatile('unburden');
		}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
			pokemon.removeVolatile('unburden');
		}
	""" 
	pass

def onModifySpe(datadic : dict):
	"""function (spe, pokemon) {
				if (!pokemon.item) {
					return this.chainModify(2);
				}
			}
	""" 
	pass
