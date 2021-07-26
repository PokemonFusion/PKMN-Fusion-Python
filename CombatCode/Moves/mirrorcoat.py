def damageCallback(**bvalues):
	"""function (pokemon) {
			if (!pokemon.volatiles['mirrorcoat']) return 0;
			return pokemon.volatiles['mirrorcoat'].damage || 1;
		}
	""" 
	pass

def beforeTurnCallback(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('mirrorcoat');
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (!source.volatiles['mirrorcoat']) return false;
			if (source.volatiles['mirrorcoat'].position === null) return false;
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
				if (effect && effect.effectType === 'Move' && source.side !== target.side && this.getCategory(effect) === 'Special') {
					this.effectData.position = source.position;
					this.effectData.damage = 2 * damage;
				}
			}
	""" 
	pass
