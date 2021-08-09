def basePowerCallback (pokemon, target, move):
	"""function (pokemon, target, move) {
			var damagedByTarget = pokemon.attackedBy.some(function (p) { return p.source === target && p.damage > 0 && p.thisTurn; });
			if (damagedByTarget) {
				this.debug('Boosted for getting hit by ' + target);
				return move.basePower * 2;
			}
			return move.basePower;
		}
	""" 
	pass