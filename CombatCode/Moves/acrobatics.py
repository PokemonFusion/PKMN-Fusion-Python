from CombatCode.diclogging import addlog


def basePowerCallback(datadic: dict):
	"""function (pokemon, target, move) {
			if (!pokemon.item) {
				this.debug("Power doubled for no item");
				return move.basePower * 2;
			}
			return move.basePower;
		}
	"""
	#pokemon = Pokemon
	pokemon = datadic['pokemon']
	#move = Moves
	move = datadic['move']

	if pokemon.hold_item is None:
		addlog(datadic, "Power doubled for no item, Acrobatics")
		return move.basePower * 2

	else:
		return move.basePower
