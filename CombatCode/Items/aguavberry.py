def onEat(**bvalues):
	"""function (pokemon) {
			this.heal(pokemon.baseMaxhp * 0.33);
			if (pokemon.getNature().minus === 'spd') {
				pokemon.addVolatile('confusion');
			}
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
			if (pokemon.hp <= pokemon.maxhp / 4 || (pokemon.hp <= pokemon.maxhp / 2 && pokemon.hasAbility('gluttony'))) {
				pokemon.eatItem();
			}
		}
	""" 
	pass
