def onFoeRedirectTarget (target, source, source2, move):
	"""function (target, source, source2, move) {
				if (!this.effectState.target.isSkyDropped() && this.validTarget(this.effectState.target, source, move.target)) {
					if (move.smartTarget)
						move.smartTarget = false;
					this.debug("Follow Me redirected target of move");
					return this.effectState.target;
				}
			}
	""" 
	pass

def onStart (target, source, effect):
	"""function (target, source, effect) {
				if ((effect === null || effect === void 0 ? void 0 : effect.id) === 'zpower') {
					this.add('-singleturn', target, 'move: Follow Me', '[zeffect]');
				}
				else {
					this.add('-singleturn', target, 'move: Follow Me');
				}
			}
	""" 
	pass

def onTry (source):
	"""function (source) {
			return this.activePerHalf > 1;
		}
	""" 
	pass