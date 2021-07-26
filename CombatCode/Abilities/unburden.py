def onAfterUseItem(**bvalues):
	"""function (item, pokemon) {
			if (pokemon !== this.effectData.target) return;
			pokemon.addVolatile('unburden');
		}
	""" 
	pass

def onTakeItem(**bvalues):
	"""function (item, pokemon) {
			pokemon.addVolatile('unburden');
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('unburden');
		}
	""" 
	pass

def onModifySpe(**bvalues):
	"""function (spe, pokemon) {
				if (!pokemon.item) {
					return this.chainModify(2);
				}
			}
	""" 
	pass
