def onTryHit(**bvalues):
	"""function (pokemon) {
			return this.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-singleturn', target, 'move: Endure');
			}
	""" 
	pass

def onDamage(**bvalues):
	"""function (damage, target, source, effect) {
				if (effect && effect.effectType === 'Move' && damage >= target.hp) {
					this.add('-activate', target, 'move: Endure');
					return target.hp - 1;
				}
			}
	""" 
	pass
