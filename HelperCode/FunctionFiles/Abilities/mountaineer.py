def onDamage (damage, target, source, effect):
	"""function (damage, target, source, effect) {
			if (effect && effect.id === 'stealthrock') {
				return False;
			}
		}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (move.type === 'Rock' && !target.activeTurns) {
				this.add('-immune', target, '[from] ability: Mountaineer');
				return null;
			}
		}
	""" 
	pass