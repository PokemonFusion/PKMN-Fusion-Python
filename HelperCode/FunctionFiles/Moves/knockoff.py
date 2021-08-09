def onAfterHit (target, source):
	"""function (target, source) {
			if (source.hp) {
				var item = target.takeItem();
				if (item) {
					this.add('-enditem', target, item.name, '[from] move: Knock Off', '[of] ' + source);
				}
			}
		}
	""" 
	pass

def onBasePower (basePower, source, target, move):
	"""function (basePower, source, target, move) {
			var item = target.getItem();
			if (!this.singleEvent('TakeItem', item, target.itemState, target, target, move, item))
				return;
			if (item.id) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass