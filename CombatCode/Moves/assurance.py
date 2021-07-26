from CombatCode.diclogging import addlog


def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			if (target.hurtThisTurn) {
				this.debug('Boosted for being damaged this turn');
				return move.basePower * 2;
			}
			return move.basePower;
		}
	"""
	target = bvalues['target']
	move = bvalues['move']
	if target.tempvals.get('hurtThisTurn', False):
		addlog(bvalues, "Boosted for target being damaged this turn, Assurance")
		return move.basepower * 2
	else:
		return move.basepower
