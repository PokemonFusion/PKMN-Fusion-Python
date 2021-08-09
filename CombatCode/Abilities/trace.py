def onStart(**bvalues):
	"""function (pokemon) {
			// n.b. only affects Hackmons
			// interaction with No Ability is complicated: https://www.smogon.com/forums/threads/pokemon-sun-moon-battle-mechanics-research.3586701/page-76#post-7790209
			if (pokemon.adjacentFoes().some(function (foeActive) { return foeActive.ability === 'noability'; })) {
				this.effectState.gaveUp = True;
			}
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (!pokemon.isStarted || this.effectState.gaveUp)
				return;
			var additionalBannedAbilities = [
				// Zen Mode included here for compatability with Gen 5-6
				'noability', 'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'zenmode',
			];
			var possibleTargets = pokemon.adjacentFoes().filter(function (target) { return (!target.getAbility().isPermanent && !additionalBannedAbilities.includes(target.ability)); });
			if (!possibleTargets.length)
				return;
			var target = this.sample(possibleTargets);
			var ability = target.getAbility();
			this.add('-ability', pokemon, ability, '[from] ability: Trace', '[of] ' + target);
			pokemon.setAbility(ability);
		}
	""" 
	pass
