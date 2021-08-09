def onImmunity(**bvalues):
	"""function (type, pokemon) {
				if (type === 'sandstorm' || type === 'hail')
					return false;
			}
	""" 
	pass

def onInvulnerability(**bvalues):
	"""function (target, source, move) {
				if (['earthquake', 'magnitude'].includes(move.id)) {
					return;
				}
				return false;
			}
	""" 
	pass

def onSourceModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
				if (move.id === 'earthquake' || move.id === 'magnitude') {
					return this.chainModify(2);
				}
			}
	""" 
	pass

def onTryMove(**bvalues):
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
