from CombatCode.diclogging import addlog


def basePowerCallback(datadic: dict):
	"""function (pokemon, target, move) {
			if (target.hurtThisTurn) {
				this.debug('Boosted for being damaged this turn');
				return move.basePower * 2;
			}
			return move.basePower;
		}
	"""
	target = datadic['target']
	move = datadic['move']
	if target.tempvals.get('hurtThisTurn', False):
		addlog(datadic, "Boosted for target being damaged this turn, Assurance")
		return move.basepower * 2
	else:
		return move.basepower
