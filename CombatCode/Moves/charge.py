def onBasePower(**bvalues):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Electric') {
					this.debug('charge boost');
					return this.chainModify(2);
				}
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (pokemon) {
				this.effectState.duration = 2;
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (pokemon) {
			this.add('-activate', pokemon, 'move: Charge');
		}
	""" 
	pass
