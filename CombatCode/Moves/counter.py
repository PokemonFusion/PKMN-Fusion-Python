def damageCallback(**bvalues):
	"""function (pokemon) {
			if (!pokemon.volatiles['counter']) return 0;
			return pokemon.volatiles['counter'].damage || 1;
		}
	""" 
	pass

def beforeTurnCallback(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('counter');
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (!source.volatiles['counter']) return false;
			if (source.volatiles['counter'].position === null) return false;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source, source2, move) {
				this.effectData.position = null;
				this.effectData.damage = 0;
			}
	""" 
	pass

def onRedirectTarget(**bvalues):
	"""function (target, source, source2) {
				if (source !== this.effectData.target) return;
				return source.side.foe.active[this.effectData.position];
			}
	""" 
	pass

def onAfterDamage(**bvalues):
	"""function (damage, target, source, effect) {
				if (effect && effect.effectType === 'Move' && source.side !== target.side && this.getCategory(effect) === 'Physical') {
					this.effectData.position = source.position;
					this.effectData.damage = 2 * damage;
				}
			}
	""" 
	pass
