def onBasePower(datadic : dict):
	"""function (basePower, attacker, defender, move) {
			if (this.isWeather('sandstorm')) {
				if (move.type === 'Rock' || move.type === 'Ground' || move.type === 'Steel') {
					this.debug('Sand Force boost');
					return this.chainModify([0x14CD, 0x1000]);
				}
			}
		}
	""" 
	pass

def onImmunity(datadic : dict):
	"""function (type, pokemon) {
			if (type === 'sandstorm') return false;
		}
	""" 
	pass
