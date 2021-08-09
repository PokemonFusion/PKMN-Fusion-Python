def onImmunity (type, pokemon):
	"""function (type, pokemon) {
				if (type === 'sandstorm' || type === 'hail')
					return false;
			}
	""" 
	pass

def onInvulnerability (target, source, move):
	"""function (target, source, move) {
				if (['earthquake', 'magnitude'].includes(move.id)) {
					return;
				}
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

def onTryMove (attacker, defender, move):
	"""function (attacker, defender, move) {
			if (attacker.removeVolatile(move.id)) {
				return;
			}
			this.add('-prepare', attacker, move.name);
			if (!this.runEvent('ChargeMove', attacker, defender, move)) {
				return;
			}
			attacker.addVolatile('twoturnmove', defender);
			return null;
		}
	""" 
	pass