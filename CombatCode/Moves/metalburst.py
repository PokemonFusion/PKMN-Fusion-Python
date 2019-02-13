def damageCallback(datadic : dict):
	"""function (pokemon) {
			if (!pokemon.volatiles['metalburst']) return 0;
			return pokemon.volatiles['metalburst'].damage || 1;
		}
	""" 
	pass

def beforeTurnCallback(datadic : dict):
	"""function (pokemon) {
			pokemon.addVolatile('metalburst');
		}
	""" 
	pass

def onTryHit(datadic : dict):
	"""function (target, source, move) {
			if (!source.volatiles['metalburst']) return false;
			if (source.volatiles['metalburst'].position === null) return false;
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target, source, source2, move) {
				this.effectData.position = null;
				this.effectData.damage = 0;
			}
	""" 
	pass

def onRedirectTarget(datadic : dict):
	"""function (target, source, source2) {
				if (source !== this.effectData.target) return;
				return source.side.foe.active[this.effectData.position];
			}
	""" 
	pass

def onAfterDamage(datadic : dict):
	"""function (damage, target, source, effect) {
				if (effect && effect.effectType === 'Move' && source.side !== target.side) {
					this.effectData.position = source.position;
					this.effectData.damage = 1.5 * damage;
				}
			}
	""" 
	pass
