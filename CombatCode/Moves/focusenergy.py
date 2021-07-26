def onStart(**bvalues):
	"""function (target, source, effect) {
				if (effect && effect.id === 'zpower') {
					this.add('-start', target, 'move: Focus Energy', '[zeffect]');
				} else if (effect && (effect.id === 'transform' || effect.id === 'imposter')) {
					this.add('-start', target, 'move: Focus Energy', '[silent]');
				} else {
					this.add('-start', target, 'move: Focus Energy');
				}
			}
	""" 
	pass

def onModifyCritRatio(**bvalues):
	"""function (critRatio) {
				return critRatio + 2;
			}
	""" 
	pass
