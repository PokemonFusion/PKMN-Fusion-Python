def onTryHit(datadic : dict):
	"""function (target, source, move) {
			if (target !== source && move.type === 'Fire') {
				move.accuracy = true;
				if (!target.addVolatile('flashfire')) {
					this.add('-immune', target, '[from] ability: Flash Fire');
				}
				return null;
			}
		}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
			pokemon.removeVolatile('flashfire');
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target) {
				this.add('-start', target, 'ability: Flash Fire');
			}
	""" 
	pass

def onModifyAtk(datadic : dict):
	"""function (atk, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('Flash Fire boost');
					return this.chainModify(1.5);
				}
			}
	""" 
	pass

def onModifySpA(datadic : dict):
	"""function (atk, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('Flash Fire boost');
					return this.chainModify(1.5);
				}
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (target) {
				this.add('-end', target, 'ability: Flash Fire', '[silent]');
			}
	""" 
	pass
