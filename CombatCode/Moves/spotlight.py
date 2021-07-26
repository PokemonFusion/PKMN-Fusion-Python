def onTryHit(**bvalues):
	"""function (target) {
			if (target.side.active.length < 2) return false;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Spotlight');
			}
	""" 
	pass

def onFoeRedirectTarget(**bvalues):
	"""function (target, source, source2, move) {
				if (this.validTarget(this.effectData.target, source, move.target)) {
					this.debug("Spotlight redirected target of move");
					return this.effectData.target;
				}
			}
	""" 
	pass
