import sys, os
sys.path.append(os.path.abspath(os.path.join('')))
from CombatCode.battledata import Pokemon
from CombatCode.pokeglobals import addlog, Moves


def basePowerCallback(datadic: dict):
	"""function (pokemon, target, move) {
			if (!pokemon.item) {
				this.debug("Power doubled for no item");
				return move.basePower * 2;
			}
			return move.basePower;
		}
	"""
	pokemon = Pokemon
	pokemon = datadic['pokemon']
	move = Moves
	move = datadic['move']

	if pokemon.hold_item is None:
		addlog(datadic, "Power doubled for no item, Acrobatics")
		return move.basePower * 2

	else:
		return move.basePower