def onAllyFaint(**bvalues):
	"""function (target) {
			if (!this.effectState.target.hp)
				return;
			var ability = target.getAbility();
			var additionalBannedAbilities = [
				'noability', 'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'wonderguard',
			];
			if (target.getAbility().isPermanent || additionalBannedAbilities.includes(target.ability))
				return;
			this.add('-ability', this.effectState.target, ability, '[from] ability: Receiver', '[of] ' + target);
			this.effectState.target.setAbility(ability);
		}
	""" 
	pass
