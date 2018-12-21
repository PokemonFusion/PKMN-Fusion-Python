def damageCallback (pokemon):
	"""function (pokemon) {
			if (!pokemon.volatiles['metalburst']) return 0;
			return pokemon.volatiles['metalburst'].damage || 1;
		}
	""" 
	pass

def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('metalburst');
		}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (!source.volatiles['metalburst']) return false;
			if (source.volatiles['metalburst'].position === null) return false;
		}
	""" 
	pass

def onStart (target, source, source2, move):
	"""function (target, source, source2, move) {
				this.effectData.position = null;
				this.effectData.damage = 0;
			}
	""" 
	pass

def onRedirectTarget (target, source, source2):
	"""function (target, source, source2) {
				if (source !== this.effectData.target) return;
				return source.side.foe.active[this.effectData.position];
			}
	""" 
	pass

def onAfterDamage (damage, target, source, effect):
	"""function (damage, target, source, effect) {
				if (effect && effect.effectType === 'Move' && source.side !== target.side) {
					this.effectData.position = source.position;
					this.effectData.damage = 1.5 * damage;
				}
			}
	""" 
	pass