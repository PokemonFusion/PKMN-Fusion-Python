def onDamage (damage, target, source, effect):
	"""function (damage, target, source, effect) {
				if ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Move' && damage >= target.hp) {
					this.add('-activate', target, 'move: Endure');
					return target.hp - 1;
				}
			}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-singleturn', target, 'move: Endure');
			}
	""" 
	pass

def onHit (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('stall');
		}
	""" 
	pass

def onPrepareHit (pokemon):
	"""function (pokemon) {
			return !!this.queue.willAct() && this.runEvent('StallMove', pokemon);
		}
	""" 
	pass