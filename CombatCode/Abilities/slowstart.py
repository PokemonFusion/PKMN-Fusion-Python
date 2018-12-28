def onStart (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('slowstart');
		}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
			delete pokemon.volatiles['slowstart'];
			this.add('-end', pokemon, 'Slow Start', '[silent]');
		}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-start', target, 'ability: Slow Start');
			}
	""" 
	pass

def onModifyAtk (atk, pokemon):
	"""function (atk, pokemon) {
				return this.chainModify(0.5);
			}
	""" 
	pass

def onModifySpe (spe, pokemon):
	"""function (spe, pokemon) {
				return this.chainModify(0.5);
			}
	""" 
	pass

def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'Slow Start');
			}
	""" 
	pass