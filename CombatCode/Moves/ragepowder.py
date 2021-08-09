def onFoeRedirectTarget(**bvalues):
	"""function (target, source, source2, move) {
				var ragePowderUser = this.effectState.target;
				if (ragePowderUser.isSkyDropped())
					return;
				if (source.runStatusImmunity('powder') && this.validTarget(ragePowderUser, source, move.target)) {
					if (move.smartTarget)
						move.smartTarget = false;
					this.debug("Rage Powder redirected target of move");
					return ragePowderUser;
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Rage Powder');
			}
	""" 
	pass

def onTry(**bvalues):
	"""function (source) {
			return this.activePerHalf > 1;
		}
	""" 
	pass
