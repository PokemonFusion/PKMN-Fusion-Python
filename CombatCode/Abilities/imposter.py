def onSwitchIn(**bvalues):
	"""function (pokemon) {
			this.effectState.switchingIn = True;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
			// Imposter does not activate when Skill Swapped or when Neutralizing Gas leaves the field
			if (!this.effectState.switchingIn)
				return;
			// copies across in doubles/triples
			// (also copies across in multibattle and diagonally in free-for-all,
			// but side.foe already takes care of those)
			var target = pokemon.side.foe.active[pokemon.side.foe.active.length - 1 - pokemon.position];
			if (target) {
				pokemon.transformInto(target, this.dex.abilities.get('imposter'));
			}
			this.effectState.switchingIn = False;
		}
	""" 
	pass
