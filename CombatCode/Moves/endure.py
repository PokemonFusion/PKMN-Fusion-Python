def onTryHit (pokemon):
	"""function (pokemon) {
			return this.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass

def onHit (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-singleturn', target, 'move: Endure');
			}
	""" 
	pass

def onDamage (damage, target, source, effect):
	"""function (damage, target, source, effect) {
				if (effect && effect.effectType === 'Move' && damage >= target.hp) {
					this.add('-activate', target, 'move: Endure');
					return target.hp - 1;
				}
			}
	""" 
	pass