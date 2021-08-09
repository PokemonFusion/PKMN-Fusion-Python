def onHit(**bvalues):
	"""function (target, source) {
			var oldAbility = source.setAbility(target.ability);
			if (oldAbility) {
				this.add('-ability', source, source.getAbility().name, '[from] move: Role Play', '[of] ' + target);
				return;
			}
			return false;
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source) {
			if (target.ability === source.ability)
				return false;
			var additionalBannedTargetAbilities = [
				// Zen Mode included here for compatability with Gen 5-6
				'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'wonderguard', 'zenmode',
			];
			if (target.getAbility().isPermanent || additionalBannedTargetAbilities.includes(target.ability) ||
				source.getAbility().isPermanent) {
				return false;
			}
		}
	""" 
	pass
