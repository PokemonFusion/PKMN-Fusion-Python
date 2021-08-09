def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('mirrorcoat');
		}
	""" 
	pass

def onDamagingHit (damage, target, source, move):
	"""function (damage, target, source, move) {
				if (!source.isAlly(target) && this.getCategory(move) === 'Special') {
					this.effectState.slot = source.getSlot();
					this.effectState.damage = 2 * damage;
				}
			}
	""" 
	pass

def onRedirectTarget (target, source, source2, move):
	"""function (target, source, source2, move) {
				if (move.id !== 'mirrorcoat')
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
			if (!pokemon.volatiles['mirrorcoat'])
				return 0;
			return pokemon.volatiles['mirrorcoat'].damage || 1;
		}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (!source.volatiles['mirrorcoat'])
				return false;
			if (source.volatiles['mirrorcoat'].slot === null)
				return false;
		}
	""" 
	pass