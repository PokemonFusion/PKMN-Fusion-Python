def onEat(**bvalues):
	"""function (pokemon) {
			var moveSlot = pokemon.moveSlots.find(function (move) { return move.pp === 0; }) ||
				pokemon.moveSlots.find(function (move) { return move.pp < move.maxpp; });
			if (!moveSlot)
				return;
			moveSlot.pp += 10;
			if (moveSlot.pp > moveSlot.maxpp)
				moveSlot.pp = moveSlot.maxpp;
			this.add('-activate', pokemon, 'item: Leppa Berry', moveSlot.move, '[consumed]');
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (!pokemon.hp)
				return;
			if (pokemon.moveSlots.some(function (move) { return move.pp === 0; })) {
				pokemon.eatItem();
			}
		}
	""" 
	pass
