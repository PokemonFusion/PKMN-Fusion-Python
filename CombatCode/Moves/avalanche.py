from CombatCode.diclogging import addlog


def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			var damagedByTarget = pokemon.attackedBy.some(function (p) { return p.source === target && p.damage > 0 && p.thisTurn; });
			if (damagedByTarget) {
				this.debug('Boosted for getting hit by ' + target);
				return move.basePower * 2;
			}
			return move.basePower;
		}
	"""
	pokemon = bvalues['pokemon']
	move = bvalues['move']
	target = bvalues['target']

	if target.getPosition() in pokemon.tempvals.get('attackers', []):
		addlog(bvalues, "Boosted for getting hit target by this turn. Avalanche")
		return move.basePower * 2

	return move.basePower

