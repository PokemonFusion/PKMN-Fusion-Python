def onHit(**bvalues):
	"""function (target, source, move) {
			var targetAbility = target.getAbility();
			var sourceAbility = source.getAbility();
			if (target.isAlly(source)) {
				this.add('-activate', source, 'move: Skill Swap', '', '', '[of] ' + target);
			}
			else {
				this.add('-activate', source, 'move: Skill Swap', targetAbility, sourceAbility, '[of] ' + target);
			}
			this.singleEvent('End', sourceAbility, source.abilityState, source);
			this.singleEvent('End', targetAbility, target.abilityState, target);
			source.ability = targetAbility.id;
			target.ability = sourceAbility.id;
			source.abilityState = { id: this.toID(source.ability), target: source };
			target.abilityState = { id: this.toID(target.ability), target: target };
			if (!target.isAlly(source))
				target.volatileStaleness = 'external';
			this.singleEvent('Start', targetAbility, source.abilityState, source);
			this.singleEvent('Start', sourceAbility, target.abilityState, target);
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source) {
			var additionalBannedAbilities = ['hungerswitch', 'illusion', 'neutralizinggas', 'wonderguard'];
			if (target.volatiles['dynamax'] ||
				target.getAbility().isPermanent || source.getAbility().isPermanent ||
				additionalBannedAbilities.includes(target.ability) || additionalBannedAbilities.includes(source.ability)) {
				return false;
			}
		}
	""" 
	pass
