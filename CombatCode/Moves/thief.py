def onAfterHit(**bvalues):
	"""function (target, source, move) {
			if (source.item || source.volatiles['gem']) {
				return;
			}
			var yourItem = target.takeItem(source);
			if (!yourItem) {
				return;
			}
			if (!this.singleEvent('TakeItem', yourItem, target.itemState, source, target, move, yourItem) ||
				!source.setItem(yourItem)) {
				target.item = yourItem.id; // bypass setItem so we don't break choicelock or anything
				return;
			}
			this.add('-enditem', target, yourItem, '[silent]', '[from] move: Thief', '[of] ' + source);
			this.add('-item', source, yourItem, '[from] move: Thief', '[of] ' + target);
		}
	""" 
	pass
