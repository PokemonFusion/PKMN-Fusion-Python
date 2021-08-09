def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('counter');
		}
	""" 
	pass

def onDamagingHit (damage, target, source, move):
	"""function (damage, target, source, move) {
				if (!source.isAlly(target) && this.getCategory(move) === 'Physical') {
					this.effectState.slot = source.getSlot();
					this.effectState.damage = 2 * damage;
				}
			}
	""" 
	pass

def onRedirectTarget (target, source, source2, move):
	"""function (target, source, source2, move) {
				if (move.id !== 'counter')
					return;
				if (source !== this.effectState.target || !this.effectState.slot)
					return;
				return this.getAtSlot(this.effectState.slot);
			}
	""" 
	pass

def onStart (target, source, move):
	"""function (target, source, move) {
				this.effectState.slot = null;
				this.effectState.damage = 0;
			}
	""" 
	pass

def damageCallback (pokemon):
	"""function (pokemon) {
			if (!pokemon.volatiles['counter'])
				return 0;
			return pokemon.volatiles['counter'].damage || 1;
		}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (!source.volatiles['counter'])
				return false;
			if (source.volatiles['counter'].slot === null)
				return false;
		}
	""" 
	pass