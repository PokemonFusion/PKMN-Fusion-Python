def onHit(**bvalues):
	"""function (target, source, move) {
			if (target.item) {
				return false;
			}
			let myItem = source.takeItem();
			if (!myItem) return false;
			if (!this.singleEvent('TakeItem', myItem, source.itemData, target, source, move, myItem) || !target.setItem(myItem)) {
				source.item = myItem.id;
				return false;
			}
			this.add('-item', target, myItem.name, '[from] move: Bestow', '[of] ' + source);
		}
	""" 
	pass
