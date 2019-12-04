from CombatCode.diclogging import addlog


def basePowerCallback(datadic: dict):
	"""function (pokemon, target, move) {
			let damagedByTarget = pokemon.attackedBy.some(p =>
				p.source === target && p.damage > 0 && p.thisTurn
			);
			if (damagedByTarget) {
				this.debug('Boosted for getting hit by ' + target);
				return move.basePower * 2;
			}
			return move.basePower;
		}
	"""
	pokemon = datadic['pokemon']
	move = datadic['move']
	target = datadic['target']

	if target.getPosition() in pokemon.tempvals.get('attackers', []):
		addlog(datadic, "Boosted for getting hit target by this turn. Avalanche")
		return move.basePower * 2

	return move.basePower

