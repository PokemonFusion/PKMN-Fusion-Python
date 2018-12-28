def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('shelltrap');
		}
	""" 
	pass

def beforeMoveCallback (pokemon):
	"""function (pokemon) {
			if (pokemon.volatiles['shelltrap'] && !pokemon.volatiles['shelltrap'].gotHit) {
				this.add('cant', pokemon, 'Shell Trap', 'Shell Trap');
				return true;
			}
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Shell Trap');
			}
	""" 
	pass

def onHit (pokemon, source, move):
	"""function (pokemon, source, move) {
				if (pokemon.side !== source.side && move.category === 'Physical') {
					pokemon.volatiles['shelltrap'].gotHit = true;
				}
			}
	""" 
	pass