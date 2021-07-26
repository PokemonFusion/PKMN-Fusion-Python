def onTryHit(**bvalues):
	"""function (target, source) {
			let bannedAbilities = ['battlebond', 'comatose', 'disguise', 'illusion', 'multitype', 'powerconstruct', 'rkssystem', 'schooling', 'shieldsdown', 'stancechange', 'wonderguard'];
			if (bannedAbilities.includes(target.ability) || bannedAbilities.includes(source.ability)) {
				return false;
			}
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
			let targetAbility = this.getAbility(target.ability);
			let sourceAbility = this.getAbility(source.ability);
			if (target.side === source.side) {
				this.add('-activate', source, 'move: Skill Swap', '', '', '[of] ' + target);
			} else {
				this.add('-activate', source, 'move: Skill Swap', targetAbility, sourceAbility, '[of] ' + target);
			}
			this.singleEvent('End', sourceAbility, source.abilityData, source);
			this.singleEvent('End', targetAbility, target.abilityData, target);
			if (targetAbility.id !== sourceAbility.id) {
				source.ability = targetAbility.id;
				target.ability = sourceAbility.id;
				source.abilityData = {id: toId(source.ability), target: source};
				target.abilityData = {id: toId(target.ability), target: target};
			}
			this.singleEvent('Start', targetAbility, source.abilityData, source);
			this.singleEvent('Start', sourceAbility, target.abilityData, target);
		}
	""" 
	pass
