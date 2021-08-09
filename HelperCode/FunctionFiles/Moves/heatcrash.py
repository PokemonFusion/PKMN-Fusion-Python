def basePowerCallback (pokemon, target):
	"""function (pokemon, target) {
			var targetWeight = target.getWeight();
			var pokemonWeight = pokemon.getWeight();
			if (pokemonWeight >= targetWeight * 5) {
				return 120;
			}
			if (pokemonWeight >= targetWeight * 4) {
				return 100;
			}
			if (pokemonWeight >= targetWeight * 3) {
				return 80;
			}
			if (pokemonWeight >= targetWeight * 2) {
				return 60;
			}
			return 40;
		}
	""" 
	pass

def onTryHit (target, pokemon, move):
	"""function (target, pokemon, move) {
			if (target.volatiles['dynamax']) {
				this.add('-fail', pokemon, 'Dynamax');
				this.attrLastMove('[still]');
				return null;
			}
		}
	""" 
	pass