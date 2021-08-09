def onEat(**bvalues):
	"""function (pokemon) {
			var moveSlot;
			if (pokemon.volatiles['leppaberry']) {
				moveSlot = pokemon.volatiles['leppaberry'].moveSlot;
				pokemon.removeVolatile('leppaberry');
			}
			else {
				var pp = 99;
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var possibleMoveSlot = _a[_i];
					if (possibleMoveSlot.pp < pp) {
						moveSlot = possibleMoveSlot;
						pp = moveSlot.pp;
					}
				}
			}
			moveSlot.pp += 5;
			if (moveSlot.pp > moveSlot.maxpp)
				moveSlot.pp = moveSlot.maxpp;
			this.add('-activate', pokemon, 'item: Mystery Berry', moveSlot.move);
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (!pokemon.hp)
				return;
			var moveSlot = pokemon.lastMove && pokemon.getMoveData(pokemon.lastMove.id);
			if (moveSlot && moveSlot.pp === 0) {
				pokemon.addVolatile('leppaberry');
				pokemon.volatiles['leppaberry'].moveSlot = moveSlot;
				pokemon.eatItem();
			}
		}
	""" 
	pass
