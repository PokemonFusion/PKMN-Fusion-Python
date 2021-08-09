def onHit (pokemon):
	"""function (pokemon) {
			var newPosition = (pokemon.position === 0 ? pokemon.side.active.length - 1 : 0);
			if (!pokemon.side.active[newPosition])
				return false;
			if (pokemon.side.active[newPosition].fainted)
				return false;
			this.swapPosition(pokemon, newPosition, '[from] move: Ally Switch');
		}
	""" 
	pass

def onTryHit (source):
	"""function (source) {
			if (source.side.active.length === 1)
				return false;
			if (source.side.active.length === 3 && source.position === 1)
				return false;
		}
	""" 
	pass