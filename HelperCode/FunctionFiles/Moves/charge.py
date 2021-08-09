def onBasePower (basePower, attacker, defender, move):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Electric') {
					this.debug('charge boost');
					return this.chainModify(2);
				}
			}
	""" 
	pass

def onRestart (pokemon):
	"""function (pokemon) {
				this.effectState.duration = 2;
			}
	""" 
	pass

def onHit (pokemon):
	"""function (pokemon) {
			this.add('-activate', pokemon, 'move: Charge');
		}
	""" 
	pass