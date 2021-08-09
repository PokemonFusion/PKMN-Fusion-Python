def onDamagingHit (damage, target, source, move):
	"""function (damage, target, source, move) {
			if (['Dark', 'Bug', 'Ghost'].includes(move.type)) {
				this.boost({ spe: 1 });
			}
		}
	""" 
	pass

def onAfterBoost (boost, target, source, effect):
	"""function (boost, target, source, effect) {
			if (effect && effect.id === 'intimidate') {
				this.boost({ spe: 1 });
			}
		}
	""" 
	pass