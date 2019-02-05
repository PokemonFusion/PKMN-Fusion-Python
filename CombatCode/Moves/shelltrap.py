def beforeTurnCallback(datadic : dict):
	"""function (pokemon) {
			pokemon.addVolatile('shelltrap');
		}
	""" 
	pass

def beforeMoveCallback(datadic : dict):
	"""function (pokemon) {
			if (pokemon.volatiles['shelltrap'] && !pokemon.volatiles['shelltrap'].gotHit) {
				this.add('cant', pokemon, 'Shell Trap', 'Shell Trap');
				return true;
			}
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Shell Trap');
			}
	""" 
	pass

def onHit(datadic : dict):
	"""function (pokemon, source, move) {
				if (pokemon.side !== source.side && move.category === 'Physical') {
					pokemon.volatiles['shelltrap'].gotHit = true;
				}
			}
	""" 
	pass
