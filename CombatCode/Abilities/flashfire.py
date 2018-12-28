def onTryHit (target, source, move):
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

def onEnd (pokemon):
	"""function (pokemon) {
			pokemon.removeVolatile('flashfire');
		}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-start', target, 'ability: Flash Fire');
			}
	""" 
	pass

def onModifyAtk (atk, attacker, defender, move):
	"""function (atk, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('Flash Fire boost');
					return this.chainModify(1.5);
				}
			}
	""" 
	pass

def onModifySpA (atk, attacker, defender, move):
	"""function (atk, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('Flash Fire boost');
					return this.chainModify(1.5);
				}
			}
	""" 
	pass

def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'ability: Flash Fire', '[silent]');
			}
	""" 
	pass