def onTryMove (attacker, defender, move):
	"""function (attacker, defender, move) {
			if (attacker.removeVolatile(move.id)) {
				return;
			}
			this.add('-prepare', attacker, move.name, defender);
			if (this.isWeather(['sunnyday', 'desolateland'])) {
				this.attrLastMove('[still]');
				this.addMove('-anim', attacker, move.name, defender);
				return;
			}
			if (!this.runEvent('ChargeMove', attacker, defender, move)) {
				return;
			}
			attacker.addVolatile('twoturnmove', defender);
			return null;
		}
	""" 
	pass

def onBasePower (basePower, pokemon, target):
	"""function (basePower, pokemon, target) {
			if (this.isWeather(['raindance', 'primordialsea', 'sandstorm', 'hail'])) {
				this.debug('weakened by weather');
				return this.chainModify(0.5);
			}
		}
	""" 
	pass