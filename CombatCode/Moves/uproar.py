def onTryHit(**bvalues):
	"""function (target) {
			for (const [i, allyActive] of target.side.active.entries()) {
				if (allyActive && allyActive.status === 'slp') allyActive.cureStatus();
				let foeActive = target.side.foe.active[i];
				if (foeActive && foeActive.status === 'slp') foeActive.cureStatus();
			}
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'Uproar');
			}
	""" 
	pass

def onResidual(**bvalues):
	"""function (target) {
				if (target.lastMove && target.lastMove.id === 'struggle') {
					// don't lock
					delete target.volatiles['uproar'];
				}
				this.add('-start', target, 'Uproar', '[upkeep]');
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'Uproar');
			}
	""" 
	pass

def onAnySetStatus(**bvalues):
	"""function (status, pokemon) {
				if (status.id === 'slp') {
					if (pokemon === this.effectData.target) {
						this.add('-fail', pokemon, 'slp', '[from] Uproar', '[msg]');
					} else {
						this.add('-fail', pokemon, 'slp', '[from] Uproar');
					}
					return null;
				}
			}
	""" 
	pass
