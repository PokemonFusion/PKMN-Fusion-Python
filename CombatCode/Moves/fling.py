def onUpdate(**bvalues):
	"""function (pokemon) {
				var item = pokemon.getItem();
				pokemon.setItem('');
				pokemon.lastItem = item.id;
				pokemon.usedItemThisTurn = true;
				this.add('-enditem', pokemon, item.name, '[from] move: Fling');
				this.runEvent('AfterUseItem', pokemon, null, null, item);
				pokemon.removeVolatile('fling');
			}
	""" 
	pass

def onPrepareHit(**bvalues):
	"""function (target, source, move) {
			if (source.ignoringItem())
				return false;
			var item = source.getItem();
			if (!this.singleEvent('TakeItem', item, source.itemState, source, source, move, item))
				return false;
			if (!item.fling)
				return false;
			move.basePower = item.fling.basePower;
			if (item.isBerry) {
				move.onHit = function (foe) {
					if (this.singleEvent('Eat', item, null, foe, null, null)) {
						this.runEvent('EatItem', foe, null, null, item);
						if (item.id === 'leppaberry')
							foe.staleness = 'external';
					}
					if (item.onEat)
						foe.ateBerry = true;
				};
			}
			else if (item.fling.effect) {
				move.onHit = item.fling.effect;
			}
			else {
				if (!move.secondaries)
					move.secondaries = [];
				if (item.fling.status) {
					move.secondaries.push({ status: item.fling.status });
				}
				else if (item.fling.volatileStatus) {
					move.secondaries.push({ volatileStatus: item.fling.volatileStatus });
				}
			}
			source.addVolatile('fling');
		}
	""" 
	pass
