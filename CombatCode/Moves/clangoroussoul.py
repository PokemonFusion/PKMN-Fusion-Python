def onHit(**bvalues):
	"""function (pokemon) {
			this.directDamage(pokemon.maxhp * 33 / 100);
		}
	""" 
	pass

def onTry(**bvalues):
	"""function (source) {
			if (source.hp <= (source.maxhp * 33 / 100) || source.maxhp === 1)
				return false;
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (pokemon, target, move) {
			if (!this.boost(move.boosts))
				return null;
			delete move.boosts;
		}
	""" 
	pass
