def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			let bp = move.basePower;
			if (pokemon.volatiles.iceball && pokemon.volatiles.iceball.hitCount) {
				bp *= Math.pow(2, pokemon.volatiles.iceball.hitCount);
			}
			if (pokemon.status !== 'slp') pokemon.addVolatile('iceball');
			if (pokemon.volatiles.defensecurl) {
				bp *= 2;
			}
			this.debug("Ice Ball bp: " + bp);
			return bp;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function () {
				this.effectData.hitCount = 1;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function () {
				this.effectData.hitCount++;
				if (this.effectData.hitCount < 5) {
					this.effectData.duration = 2;
				}
			}
	""" 
	pass

def onResidual(**bvalues):
	"""function (target) {
				if (target.lastMove && target.lastMove.id === 'struggle') {
					// don't lock
					delete target.volatiles['iceball'];
				}
			}
	""" 
	pass
