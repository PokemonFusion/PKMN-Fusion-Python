def onTryHit(datadic : dict):
	"""function (pokemon) {
			let bannedAbilities = ['battlebond', 'comatose', 'disguise', 'insomnia', 'multitype', 'powerconstruct', 'rkssystem', 'schooling', 'shieldsdown', 'stancechange', 'truant'];
			if (bannedAbilities.includes(pokemon.ability)) {
				return false;
			}
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (pokemon) {
			let oldAbility = pokemon.setAbility('insomnia');
			if (oldAbility) {
				this.add('-ability', pokemon, 'Insomnia', '[from] move: Worry Seed');
				if (pokemon.status === 'slp') {
					pokemon.cureStatus();
				}
				return;
			}
			return false;
		}
	""" 
	pass
