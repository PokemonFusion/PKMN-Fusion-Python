def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.hp <= pokemon.maxhp / 2) {
				pokemon.eatItem();
			}
		}
	""" 
	pass

def onTryEatItem(**bvalues):
	"""function (item, pokemon) {
			if (!this.runEvent('TryHeal', pokemon)) return False;
		}
	""" 
	pass

def onEat(**bvalues):
	"""function (pokemon) {
			this.heal(pokemon.maxhp / 4);
		}
	""" 
	pass
