def basePowerCallback(datadic : dict):
	"""function (pokemon, target, move) {
			// @ts-ignore
			return 5 + Math.floor(move.allies.shift().template.baseStats.atk / 10);
		}
	""" 
	pass

def onModifyMove(datadic : dict):
	"""function (move, pokemon) {
			move.allies = pokemon.side.pokemon.filter(ally => ally === pokemon || !ally.fainted && !ally.status);
			move.multihit = move.allies.length;
		}
	""" 
	pass
