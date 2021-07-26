def onDamage(**bvalues):
	"""function (damage, target, source, effect) {
			if (effect && effect.id === 'stealthrock') {
				return false;
			}
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (move.type === 'Rock' && !target.activeTurns) {
				this.add('-immune', target, '[from] ability: Mountaineer');
				return null;
			}
		}
	""" 
	pass
