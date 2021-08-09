def onAfterUseItem (item, pokemon):
	"""function (item, pokemon) {
			if (pokemon !== this.effectState.target)
				return;
			pokemon.addVolatile('unburden');
		}
	""" 
	pass

def onTakeItem (item, pokemon):
	"""function (item, pokemon) {
			pokemon.addVolatile('unburden');
		}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
			pokemon.removeVolatile('unburden');
		}
	""" 
	pass

def onModifySpe (spe, pokemon):
	"""function (spe, pokemon) {
				if (!pokemon.item && !pokemon.ignoringAbility()) {
					return this.chainModify(2);
				}
			}
	""" 
	pass