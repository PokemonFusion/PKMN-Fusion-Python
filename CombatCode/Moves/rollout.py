def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			var bp = move.basePower;
			if (pokemon.volatiles['rollout'] && pokemon.volatiles['rollout'].hitCount) {
				bp *= Math.pow(2, pokemon.volatiles['rollout'].hitCount);
			}
			if (pokemon.status !== 'slp')
				pokemon.addVolatile('rollout');
			if (pokemon.volatiles['defensecurl']) {
				bp *= 2;
			}
			this.debug("Rollout bp: " + bp);
			return bp;
		}
	""" 
	pass

def onResidual(**bvalues):
	"""function (target) {
				if (target.lastMove && target.lastMove.id === 'struggle') {
					// don't lock
					delete target.volatiles['rollout'];
				}
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function () {
				this.effectState.hitCount++;
				if (this.effectState.hitCount < 5) {
					this.effectState.duration = 2;
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function () {
				this.effectState.hitCount = 1;
			}
	""" 
	pass
