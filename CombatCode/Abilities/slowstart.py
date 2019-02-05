def onStart(datadic : dict):
	"""function (pokemon) {
			pokemon.addVolatile('slowstart');
		}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
			delete pokemon.volatiles['slowstart'];
			this.add('-end', pokemon, 'Slow Start', '[silent]');
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target) {
				this.add('-start', target, 'ability: Slow Start');
			}
	""" 
	pass

def onModifyAtk(datadic : dict):
	"""function (atk, pokemon) {
				return this.chainModify(0.5);
			}
	""" 
	pass

def onModifySpe(datadic : dict):
	"""function (spe, pokemon) {
				return this.chainModify(0.5);
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (target) {
				this.add('-end', target, 'Slow Start');
			}
	""" 
	pass
