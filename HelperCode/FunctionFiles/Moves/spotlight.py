def onFoeRedirectTarget (target, source, source2, move):
	"""function (target, source, source2, move) {
				if (this.validTarget(this.effectState.target, source, move.target)) {
					this.debug("Spotlight redirected target of move");
					return this.effectState.target;
				}
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Spotlight');
			}
	""" 
	pass

def onTryHit (target):
	"""function (target) {
			if (this.activePerHalf === 1)
				return false;
		}
	""" 
	pass