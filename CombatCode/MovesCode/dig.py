def onTryMove (attacker, defender, move):
	"""function (attacker, defender, move) {
			if (attacker.removeVolatile(move.id)) {
				return;
			}
			this.add('-prepare', attacker, move.name, defender);
			if (!this.runEvent('ChargeMove', attacker, defender, move)) {
				return;
			}
			attacker.addVolatile('twoturnmove', defender);
			return null;
		}
	""" 
	pass

def onImmunity (type, pokemon):
	"""function (type, pokemon) {
				if (type === 'sandstorm' || type === 'hail') return false;
			}
	""" 
	pass

def onTryImmunity (target, source, move):
	"""function (target, source, move) {
				if (move.id === 'earthquake' || move.id === 'magnitude' || move.id === 'helpinghand') {
					return;
				}
				if (source.hasAbility('noguard') || target.hasAbility('noguard')) {
					return;
				}
				if (source.volatiles['lockon'] && target === source.volatiles['lockon'].source) return;
				return false;
			}
	""" 
	pass

def onSourceModifyDamage (damage, source, target, move):
	"""function (damage, source, target, move) {
				if (move.id === 'earthquake' || move.id === 'magnitude') {
					return this.chainModify(2);
				}
			}
	""" 
	pass