def onPrepareHit (target, source, move):
	"""function (target, source, move) {
			if (source.ignoringItem()) return false;
			let item = source.getItem();
			if (!this.singleEvent('TakeItem', item, source.itemData, source, source, move, item)) return false;
			if (!item.fling) return false;
			move.basePower = item.fling.basePower;
			if (item.isBerry) {
				move.onHit = function (foe) {
					if (this.singleEvent('Eat', item, null, foe, null, null)) {
						this.runEvent('EatItem', foe, null, null, item);
					}
					if (item.onEat) foe.ateBerry = true;
				};
			} else if (item.fling.effect) {
				move.onHit = item.fling.effect;
			} else {
				if (!move.secondaries) move.secondaries = [];
				if (item.fling.status) {
					move.secondaries.push({status: item.fling.status});
				} else if (item.fling.volatileStatus) {
					move.secondaries.push({volatileStatus: item.fling.volatileStatus});
				}
			}
			source.setItem('');
			source.lastItem = item.id;
			source.usedItemThisTurn = true;
			this.add("-enditem", source, item.name, '[from] move: Fling');
			this.runEvent('AfterUseItem', source, null, null, item);
		}
	""" 
	pass