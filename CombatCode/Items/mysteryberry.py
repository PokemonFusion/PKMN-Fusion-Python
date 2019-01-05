def onUpdate (pokemon):
	"""function (pokemon) {
			if (!pokemon.hp) return;
			let moveSlot = pokemon.lastMove && pokemon.getMoveData(pokemon.lastMove.id);
			if (moveSlot && moveSlot.pp === 0) {
				pokemon.addVolatile('leppaberry');
				pokemon.volatiles['leppaberry'].moveSlot = moveSlot;
				pokemon.eatItem();
			}
		}
	""" 
	pass

def onEat (pokemon):
	"""function (pokemon) {
			let moveSlot;
			if (pokemon.volatiles['leppaberry']) {
				moveSlot = pokemon.volatiles['leppaberry'].moveSlot;
				pokemon.removeVolatile('leppaberry');
			} else {
				let pp = 99;
				for (const possibleMoveSlot of pokemon.moveSlots) {
					if (possibleMoveSlot.pp < pp) {
						moveSlot = possibleMoveSlot;
						pp = moveSlot.pp;
					}
				}
			}
			moveSlot.pp += 5;
			if (moveSlot.pp > moveSlot.maxpp) moveSlot.pp = moveSlot.maxpp;
			this.add('-activate', pokemon, 'item: Mystery Berry', moveSlot.move);
			if (pokemon.item !== 'leppaberry') {
				let foeActive = pokemon.side.foe.active;
				let foeIsStale = False;
				for (let i = 0; i < foeActive.length; i++) {
					if (foeActive[i].isStale >= 2) {
						foeIsStale = True;
						break;
					}
				}
				if (!foeIsStale) return;
			}
			pokemon.isStale = 2;
			pokemon.isStaleSource = 'useleppa';
		}
	""" 
	pass