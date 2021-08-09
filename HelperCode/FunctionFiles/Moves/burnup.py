def onTryMove (pokemon, target, move):
	"""function (pokemon, target, move) {
			if (pokemon.hasType('Fire'))
				return;
			this.add('-fail', pokemon, 'move: Burn Up');
			this.attrLastMove('[still]');
			return null;
		}
	""" 
	pass

def onHit (pokemon):
	"""function (pokemon) {
				pokemon.setType(pokemon.getTypes(true).map(function (type) { return type === "Fire" ? "???" : type; }));
				this.add('-start', pokemon, 'typechange', pokemon.types.join('/'), '[from] move: Burn Up');
			}
	""" 
	pass