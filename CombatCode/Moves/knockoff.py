def onBasePower(**bvalues):
	"""function (basePower, source, target, move) {
			let item = target.getItem();
			if (!this.singleEvent('TakeItem', item, target.itemData, target, source, move, item)) return;
			if (item.id) {
				return this.chainModify(1.5);
			}
		}
	""" 
	pass

def onAfterHit(**bvalues):
	"""function (target, source) {
			if (source.hp) {
				let item = target.takeItem();
				if (item) {
					this.add('-enditem', target, item.name, '[from] move: Knock Off', '[of] ' + source);
				}
			}
		}
	""" 
	pass
