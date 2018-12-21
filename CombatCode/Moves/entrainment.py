def onTryHit (target, source):
	"""function (target, source) {
			if (target === source) return false;
			let bannedTargetAbilities = ['battlebond', 'comatose', 'disguise', 'multitype', 'powerconstruct', 'rkssystem', 'schooling', 'shieldsdown', 'stancechange', 'truant'];
			let bannedSourceAbilities = ['battlebond', 'comatose', 'disguise', 'flowergift', 'forecast', 'illusion', 'imposter', 'multitype', 'powerconstruct', 'powerofalchemy', 'receiver', 'rkssystem', 'schooling', 'shieldsdown', 'stancechange', 'trace', 'zenmode'];
			if (bannedTargetAbilities.includes(target.ability) || bannedSourceAbilities.includes(source.ability) || target.ability === source.ability) {
				return false;
			}
		}
	""" 
	pass

def onHit (target, source):
	"""function (target, source) {
			let oldAbility = target.setAbility(source.ability);
			if (oldAbility) {
				this.add('-ability', target, this.getAbility(target.ability).name, '[from] move: Entrainment');
				return;
			}
			return false;
		}
	""" 
	pass