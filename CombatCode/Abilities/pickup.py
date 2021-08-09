def onResidual(**bvalues):
	"""function (pokemon) {
			if (pokemon.item)
				return;
			var pickupTargets = this.getAllActive().filter(function (target) { return (target.lastItem && target.usedItemThisTurn && pokemon.isAdjacent(target)); });
			if (!pickupTargets.length)
				return;
			var randomTarget = this.sample(pickupTargets);
			var item = randomTarget.lastItem;
			randomTarget.lastItem = '';
			this.add('-item', pokemon, this.dex.items.get(item), '[from] ability: Pickup');
			pokemon.setItem(item);
		}
	""" 
	pass
