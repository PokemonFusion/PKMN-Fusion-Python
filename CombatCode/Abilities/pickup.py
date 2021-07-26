def onResidual(**bvalues):
	"""function (pokemon) {
			if (pokemon.item) return;
			let pickupTargets = [];
			for (const target of pokemon.side.active.concat(pokemon.side.foe.active)) {
				if (target.lastItem && target.usedItemThisTurn && this.isAdjacent(pokemon, target)) {
					pickupTargets.push(target);
				}
			}
			if (!pickupTargets.length) return;
			let randomTarget = this.sample(pickupTargets);
			pokemon.setItem(randomTarget.lastItem);
			randomTarget.lastItem = '';
			let item = pokemon.getItem();
			this.add('-item', pokemon, item, '[from] ability: Pickup');
		}
	""" 
	pass
