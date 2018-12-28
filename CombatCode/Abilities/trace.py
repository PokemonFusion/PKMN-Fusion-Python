def onStart (pokemon):
	"""function (pokemon) {
			if (pokemon.side.foe.active.some(foeActive => foeActive && this.isAdjacent(pokemon, foeActive) && foeActive.ability === 'noability')) {
				this.effectData.gaveUp = true;
			}
		}
	""" 
	pass

def onUpdate (pokemon):
	"""function (pokemon) {
			if (!pokemon.isStarted || this.effectData.gaveUp) return;
			let possibleTargets = pokemon.side.foe.active.filter(foeActive => foeActive && this.isAdjacent(pokemon, foeActive));
			while (possibleTargets.length) {
				let rand = 0;
				if (possibleTargets.length > 1) rand = this.random(possibleTargets.length);
				let target = possibleTargets[rand];
				let ability = this.getAbility(target.ability);
				let bannedAbilities = ['noability', 'battlebond', 'comatose', 'disguise', 'flowergift', 'forecast', 'illusion', 'imposter', 'multitype', 'powerconstruct', 'powerofalchemy', 'receiver', 'rkssystem', 'schooling', 'shieldsdown', 'stancechange', 'trace', 'zenmode'];
				if (bannedAbilities.includes(target.ability)) {
					possibleTargets.splice(rand, 1);
					continue;
				}
				this.add('-ability', pokemon, ability, '[from] ability: Trace', '[of] ' + target);
				pokemon.setAbility(ability);
				return;
			}
		}
	""" 
	pass