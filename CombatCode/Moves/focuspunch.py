def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('focuspunch');
		}
	""" 
	pass

def beforeMoveCallback (pokemon):
	"""function (pokemon) {
			if (pokemon.volatiles['focuspunch'] && pokemon.volatiles['focuspunch'].lostFocus) {
				this.add('cant', pokemon, 'Focus Punch', 'Focus Punch');
				return true;
			}
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Focus Punch');
			}
	""" 
	pass

def onHit (pokemon, source, move):
	"""function (pokemon, source, move) {
				if (move.category !== 'Status') {
					pokemon.volatiles['focuspunch'].lostFocus = true;
				}
			}
	""" 
	pass