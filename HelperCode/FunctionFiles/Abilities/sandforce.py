def onBasePower (basePower, attacker, defender, move):
	"""function (basePower, attacker, defender, move) {
			if (this.field.isWeather('sandstorm')) {
				if (move.type === 'Rock' || move.type === 'Ground' || move.type === 'Steel') {
					this.debug('Sand Force boost');
					return this.chainModify([5325, 4096]);
				}
			}
		}
	""" 
	pass

def onImmunity (type, pokemon):
	"""function (type, pokemon) {
			if (type === 'sandstorm')
				return False;
		}
	""" 
	pass