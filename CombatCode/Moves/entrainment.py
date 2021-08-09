def onHit(**bvalues):
	"""function (target, source) {
			var oldAbility = target.setAbility(source.ability);
			if (oldAbility) {
				this.add('-ability', target, target.getAbility().name, '[from] move: Entrainment');
				if (!target.isAlly(source))
					target.volatileStaleness = 'external';
				return;
			}
			return false;
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source) {
			if (target === source || target.volatiles['dynamax'])
				return false;
			var additionalBannedSourceAbilities = [
				// Zen Mode included here for compatability with Gen 5-6
				'flowergift', 'forecast', 'hungerswitch', 'illusion', 'imposter', 'neutralizinggas', 'powerofalchemy', 'receiver', 'trace', 'zenmode',
			];
			if (target.ability === source.ability ||
				target.getAbility().isPermanent || target.ability === 'truant' ||
				source.getAbility().isPermanent || additionalBannedSourceAbilities.includes(source.ability)) {
				return false;
			}
		}
	""" 
	pass
