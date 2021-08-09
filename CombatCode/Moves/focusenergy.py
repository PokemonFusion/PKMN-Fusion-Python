def onModifyCritRatio(**bvalues):
	"""function (critRatio) {
				return critRatio + 2;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source, effect) {
				if ((effect === null || effect === void 0 ? void 0 : effect.id) === 'zpower') {
					this.add('-start', target, 'move: Focus Energy', '[zeffect]');
				}
				else if (effect && (['imposter', 'psychup', 'transform'].includes(effect.id))) {
					this.add('-start', target, 'move: Focus Energy', '[silent]');
				}
				else {
					this.add('-start', target, 'move: Focus Energy');
				}
			}
	""" 
	pass
