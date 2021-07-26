def onStart(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('slowstart');
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			delete pokemon.volatiles['slowstart'];
			this.add('-end', pokemon, 'Slow Start', '[silent]');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'ability: Slow Start');
			}
	""" 
	pass

def onModifyAtk(**bvalues):
	"""function (atk, pokemon) {
				return this.chainModify(0.5);
			}
	""" 
	pass

def onModifySpe(**bvalues):
	"""function (spe, pokemon) {
				return this.chainModify(0.5);
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'Slow Start');
			}
	""" 
	pass
