def onHit (pokemon):
	"""function (pokemon) {
			var oldAbility = pokemon.setAbility('simple');
			if (oldAbility) {
				this.add('-ability', pokemon, 'Simple', '[from] move: Simple Beam');
				return;
			}
			return false;
		}
	""" 
	pass

def onTryHit (target):
	"""function (target) {
			if (target.getAbility().isPermanent || target.ability === 'simple' || target.ability === 'truant') {
				return false;
			}
		}
	""" 
	pass