def onAnySetStatus (status, pokemon):
	"""function (status, pokemon) {
				if (status.id === 'slp') {
					if (pokemon === this.effectState.target) {
						this.add('-fail', pokemon, 'slp', '[from] Uproar', '[msg]');
					}
					else {
						this.add('-fail', pokemon, 'slp', '[from] Uproar');
					}
					return null;
				}
			}
	""" 
	pass

def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'Uproar');
			}
	""" 
	pass

def onResidual (target):
	"""function (target) {
				if (target.volatiles['throatchop']) {
					target.removeVolatile('uproar');
					return;
				}
				if (target.lastMove && target.lastMove.id === 'struggle') {
					// don't lock
					delete target.volatiles['uproar'];
				}
				this.add('-start', target, 'Uproar', '[upkeep]');
			}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-start', target, 'Uproar');
			}
	""" 
	pass

def onTryHit (target):
	"""function (target) {
			var activeTeam = target.side.activeTeam();
			var foeActiveTeam = target.side.foe.activeTeam();
			for (var _i = 0, _a = activeTeam.entries(); _i < _a.length; _i++) {
				var _b = _a[_i], i = _b[0], allyActive = _b[1];
				if (allyActive && allyActive.status === 'slp')
					allyActive.cureStatus();
				var foeActive = foeActiveTeam[i];
				if (foeActive && foeActive.status === 'slp')
					foeActive.cureStatus();
			}
		}
	""" 
	pass