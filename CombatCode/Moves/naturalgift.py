def onModifyType(**bvalues):
	"""function (move, pokemon) {
			if (pokemon.ignoringItem())
				return;
			var item = pokemon.getItem();
			if (!item.naturalGift)
				return;
			move.type = item.naturalGift.type;
		}
	""" 
	pass

def onPrepareHit(**bvalues):
	"""function (target, pokemon, move) {
			if (pokemon.ignoringItem())
				return false;
			var item = pokemon.getItem();
			if (!item.naturalGift)
				return false;
			move.basePower = item.naturalGift.basePower;
			pokemon.setItem('');
			pokemon.lastItem = item.id;
			pokemon.usedItemThisTurn = true;
			this.runEvent('AfterUseItem', pokemon, null, null, item);
		}
	""" 
	pass
