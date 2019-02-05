def onTryHit(datadic : dict):
	"""function (pokemon) {
			return this.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target) {
				this.add('-singleturn', target, 'move: Endure');
			}
	""" 
	pass

def onDamage(datadic : dict):
	"""function (damage, target, source, effect) {
				if (effect && effect.effectType === 'Move' && damage >= target.hp) {
					this.add('-activate', target, 'move: Endure');
					return target.hp - 1;
				}
			}
	""" 
	pass
