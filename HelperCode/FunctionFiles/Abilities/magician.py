def onAfterMoveSecondarySelf (source, target, move):
	"""function (source, target, move) {
			if (!move || !target)
				return;
			if (target !== source && move.category !== 'Status') {
				if (source.item || source.volatiles['gem'] || move.id === 'fling')
					return;
				var yourItem = target.takeItem(source);
				if (!yourItem)
					return;
				if (!source.setItem(yourItem)) {
					target.item = yourItem.id; // bypass setItem so we don't break choicelock or anything
					return;
				}
				this.add('-item', source, yourItem, '[from] ability: Magician', '[of] ' + target);
			}
		}
	""" 
	pass