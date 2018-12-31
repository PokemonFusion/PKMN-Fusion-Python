def onUpdate (pokemon):
	"""function (pokemon) {
			if (!pokemon.hp) return;
			if (pokemon.moveSlots.some(move => move.pp === 0)) {
				pokemon.eatItem();
			}
		}
	""" 
	pass

def onEat (pokemon):
	"""function (pokemon) {
			let moveSlot = pokemon.moveSlots.find(move => move.pp === 0) ||
				pokemon.moveSlots.find(move => move.pp < move.maxpp);
			if (!moveSlot) return;
			moveSlot.pp += 10;
			if (moveSlot.pp > moveSlot.maxpp) moveSlot.pp = moveSlot.maxpp;
			this.add('-activate', pokemon, 'item: Leppa Berry', moveSlot.move, '[consumed]');
			if (pokemon.item !== 'leppaberry') {
				let foeIsStale = False;
				for (const foeActive of pokemon.side.foe.active) {
					if (foeActive.hp && foeActive.isStale >= 2) {
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