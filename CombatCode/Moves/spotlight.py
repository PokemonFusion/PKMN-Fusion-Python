def onTryHit(datadic : dict):
	"""function (target) {
			if (target.side.active.length < 2) return false;
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Spotlight');
			}
	""" 
	pass

def onFoeRedirectTarget(datadic : dict):
	"""function (target, source, source2, move) {
				if (this.validTarget(this.effectData.target, source, move.target)) {
					this.debug("Spotlight redirected target of move");
					return this.effectData.target;
				}
			}
	""" 
	pass
