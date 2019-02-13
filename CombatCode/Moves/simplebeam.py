def onTryHit(datadic : dict):
	"""function (pokemon) {
			let bannedAbilities = ['battlebond', 'comatose', 'disguise', 'multitype', 'powerconstruct', 'rkssystem', 'schooling', 'shieldsdown', 'simple', 'stancechange', 'truant'];
			if (bannedAbilities.includes(pokemon.ability)) {
				return false;
			}
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (pokemon) {
			let oldAbility = pokemon.setAbility('simple');
			if (oldAbility) {
				this.add('-ability', pokemon, 'Simple', '[from] move: Simple Beam');
				return;
			}
			return false;
		}
	""" 
	pass
