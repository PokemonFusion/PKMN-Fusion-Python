def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (target !== source && move.type === 'Fire') {
				move.accuracy = True;
				if (!target.addVolatile('flashfire')) {
					this.add('-immune', target, '[from] ability: Flash Fire');
				}
				return null;
			}
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			pokemon.removeVolatile('flashfire');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'ability: Flash Fire');
			}
	""" 
	pass

def onModifyAtk(**bvalues):
	"""function (atk, attacker, defender, move) {
				if (move.type === 'Fire' && attacker.hasAbility('flashfire')) {
					this.debug('Flash Fire boost');
					return this.chainModify(1.5);
				}
			}
	""" 
	pass

def onModifySpA(**bvalues):
	"""function (atk, attacker, defender, move) {
				if (move.type === 'Fire' && attacker.hasAbility('flashfire')) {
					this.debug('Flash Fire boost');
					return this.chainModify(1.5);
				}
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'ability: Flash Fire', '[silent]');
			}
	""" 
	pass
