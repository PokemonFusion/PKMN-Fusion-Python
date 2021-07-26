def onTryHit(**bvalues):
	"""function (target) {
			if (target.side.active.length < 2) return false;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Rage Powder');
			}
	""" 
	pass

def onFoeRedirectTarget(**bvalues):
	"""function (target, source, source2, move) {
				if (!this.effectData.target.isSkyDropped() && source.runStatusImmunity('powder') && this.validTarget(this.effectData.target, source, move.target)) {
					this.debug("Rage Powder redirected target of move");
					return this.effectData.target;
				}
			}
	""" 
	pass
