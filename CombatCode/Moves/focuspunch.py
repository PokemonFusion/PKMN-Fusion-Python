def beforeMoveCallback(**bvalues):
	"""function (pokemon) {
			if (pokemon.volatiles['focuspunch'] && pokemon.volatiles['focuspunch'].lostFocus) {
				this.add('cant', pokemon, 'Focus Punch', 'Focus Punch');
				return true;
			}
		}
	""" 
	pass

def beforeTurnCallback(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('focuspunch');
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (pokemon, source, move) {
				if (move.category !== 'Status') {
					pokemon.volatiles['focuspunch'].lostFocus = true;
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Focus Punch');
			}
	""" 
	pass

def onTryAddVolatile(**bvalues):
	"""function (status, pokemon) {
				if (status.id === 'flinch')
					return null;
			}
	""" 
	pass
