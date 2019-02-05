def onUpdate(datadic : dict):
	"""function (pokemon) {
			if (pokemon.hp <= pokemon.maxhp / 2) {
				pokemon.eatItem();
			}
		}
	""" 
	pass

def onTryEatItem(datadic : dict):
	"""function (item, pokemon) {
			if (!this.runEvent('TryHeal', pokemon)) return False;
		}
	""" 
	pass

def onEat(datadic : dict):
	"""function (pokemon) {
			this.heal(pokemon.maxhp / 4);
		}
	""" 
	pass
