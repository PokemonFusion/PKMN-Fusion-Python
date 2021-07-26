def onTryHit(**bvalues):
	"""function (target) {
			if (target.side.active.length < 2) return false;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source, effect) {
				if (effect && effect.id === 'zpower') {
					this.add('-singleturn', target, 'move: Follow Me', '[zeffect]');
				} else {
					this.add('-singleturn', target, 'move: Follow Me');
				}
			}
	""" 
	pass

def onFoeRedirectTarget(**bvalues):
	"""function (target, source, source2, move) {
				if (!this.effectData.target.isSkyDropped() && this.validTarget(this.effectData.target, source, move.target)) {
					this.debug("Follow Me redirected target of move");
					return this.effectData.target;
				}
			}
	""" 
	pass
