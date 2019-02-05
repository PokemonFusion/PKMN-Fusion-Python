def onHit(datadic : dict):
	"""function (pokemon) {
			this.add('-activate', pokemon, 'move: Charge');
		}
	""" 
	pass

def onRestart(datadic : dict):
	"""function (pokemon) {
				this.effectData.duration = 2;
			}
	""" 
	pass

def onBasePower(datadic : dict):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Electric') {
					this.debug('charge boost');
					return this.chainModify(2);
				}
			}
	""" 
	pass
