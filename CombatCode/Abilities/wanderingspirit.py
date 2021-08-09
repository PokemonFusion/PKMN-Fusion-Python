def onDamagingHit(**bvalues):
	"""function (damage, target, source, move) {
			var additionalBannedAbilities = ['hungerswitch', 'illusion', 'neutralizinggas', 'wonderguard'];
			if (source.getAbility().isPermanent || additionalBannedAbilities.includes(source.ability) ||
				target.volatiles['dynamax']) {
				return;
			}
			if (this.checkMoveMakesContact(move, source, target)) {
				var sourceAbility = source.setAbility('wanderingspirit', target);
				if (!sourceAbility)
					return;
				if (target.isAlly(source)) {
					this.add('-activate', target, 'Skill Swap', '', '', '[of] ' + source);
				}
				else {
					this.add('-activate', target, 'ability: Wandering Spirit', this.dex.abilities.get(sourceAbility).name, 'Wandering Spirit', '[of] ' + source);
				}
				target.setAbility(sourceAbility);
			}
		}
	""" 
	pass
