def onEat(**bvalues):
	"""function () { }
	""" 
	pass

def onFractionalPriority(**bvalues):
	"""function (priority, pokemon) {
			if (priority <= 0 &&
				(pokemon.hp <= pokemon.maxhp / 4 || (pokemon.hp <= pokemon.maxhp / 2 && pokemon.hasAbility('gluttony')))) {
				if (pokemon.eatItem()) {
					this.add('-activate', pokemon, 'item: Custap Berry', '[consumed]');
					return 0.1;
				}
			}
		}
	""" 
	pass
