def onHit (target, source, move):
	"""function (target, source, move) {
			var yourItem = target.takeItem(source);
			var myItem = source.takeItem();
			if (target.item || source.item || (!yourItem && !myItem)) {
				if (yourItem)
					target.item = yourItem.id;
				if (myItem)
					source.item = myItem.id;
				return false;
			}
			if ((myItem && !this.singleEvent('TakeItem', myItem, source.itemState, target, source, move, myItem)) ||
				(yourItem && !this.singleEvent('TakeItem', yourItem, target.itemState, source, target, move, yourItem))) {
				if (yourItem)
					target.item = yourItem.id;
				if (myItem)
					source.item = myItem.id;
				return false;
			}
			this.add('-activate', source, 'move: Trick', '[of] ' + target);
			if (myItem) {
				target.setItem(myItem);
				this.add('-item', target, myItem, '[from] move: Switcheroo');
			}
			else {
				this.add('-enditem', target, yourItem, '[silent]', '[from] move: Switcheroo');
			}
			if (yourItem) {
				source.setItem(yourItem);
				this.add('-item', source, yourItem, '[from] move: Switcheroo');
			}
			else {
				this.add('-enditem', source, myItem, '[silent]', '[from] move: Switcheroo');
			}
		}
	""" 
	pass

def onTryImmunity (target):
	"""function (target) {
			return !target.hasAbility('stickyhold');
		}
	""" 
	pass