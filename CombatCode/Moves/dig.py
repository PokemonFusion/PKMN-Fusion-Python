def onTryMove(datadic : dict):
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

def onImmunity(datadic : dict):
	"""function (type, pokemon) {
				if (type === 'sandstorm' || type === 'hail') return false;
			}
	""" 
	pass

def onTryImmunity(datadic : dict):
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

def onSourceModifyDamage(datadic : dict):
	"""function (damage, source, target, move) {
				if (move.id === 'earthquake' || move.id === 'magnitude') {
					return this.chainModify(2);
				}
			}
	""" 
	pass
