def onHit(**bvalues):
	"""function (pokemon) {
			this.add('-activate', pokemon, 'move: Charge');
		}
	""" 
	pass

def onRestart(**bvalues):
	"""function (pokemon) {
				this.effectData.duration = 2;
			}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Electric') {
					this.debug('charge boost');
					return this.chainModify(2);
				}
			}
	""" 
	pass
