def onTryHit (target, source):
	"""function (target, source) {
			let bannedTargetAbilities = ['battlebond', 'comatose', 'disguise', 'flowergift', 'forecast', 'illusion', 'imposter', 'multitype', 'powerconstruct', 'powerofalchemy', 'receiver', 'rkssystem', 'schooling', 'shieldsdown', 'stancechange', 'trace', 'wonderguard', 'zenmode'];
			let bannedSourceAbilities = ['battlebond', 'comatose', 'disguise', 'multitype', 'powerconstruct', 'rkssystem', 'schooling', 'shieldsdown', 'stancechange'];
			if (bannedTargetAbilities.includes(target.ability) || bannedSourceAbilities.includes(source.ability) || target.ability === source.ability) {
				return false;
			}
		}
	""" 
	pass

def onHit (target, source):
	"""function (target, source) {
			let oldAbility = source.setAbility(target.ability);
			if (oldAbility) {
				this.add('-ability', source, this.getAbility(source.ability).name, '[from] move: Role Play', '[of] ' + target);
				return;
			}
			return false;
		}
	""" 
	pass