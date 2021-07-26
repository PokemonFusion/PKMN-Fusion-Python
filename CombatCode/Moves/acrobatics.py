from CombatCode.diclogging import addlog


def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			if (!pokemon.item) {
				this.debug("Power doubled for no item");
				return move.basePower * 2;
			}
			return move.basePower;
		}
	"""
	pokemon = bvalues['pokemon']
	move = bvalues['move']

	if pokemon.hold_item is None:
		addlog(bvalues, "Power doubled for holding no item, Acrobatics")
		return move.basePower * 2

	else:
		return move.basePower
