def beforeTurnCallback(datadic : dict):
	"""function (pokemon) {
			pokemon.addVolatile('focuspunch');
		}
	""" 
	pass

def beforeMoveCallback(datadic : dict):
	"""function (pokemon) {
			if (pokemon.volatiles['focuspunch'] && pokemon.volatiles['focuspunch'].lostFocus) {
				this.add('cant', pokemon, 'Focus Punch', 'Focus Punch');
				return true;
			}
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Focus Punch');
			}
	""" 
	pass

def onHit(datadic : dict):
	"""function (pokemon, source, move) {
				if (move.category !== 'Status') {
					pokemon.volatiles['focuspunch'].lostFocus = true;
				}
			}
	""" 
	pass
