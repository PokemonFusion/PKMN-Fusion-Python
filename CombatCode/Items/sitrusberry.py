def onEat(**bvalues):
	"""function (pokemon) {
			this.heal(pokemon.baseMaxhp / 4);
		}
	""" 
	pass

def onTryEatItem(**bvalues):
	"""function (item, pokemon) {
			if (!this.runEvent('TryHeal', pokemon))
				return false;
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.hp <= pokemon.maxhp / 2) {
				pokemon.eatItem();
			}
		}
	""" 
	pass
