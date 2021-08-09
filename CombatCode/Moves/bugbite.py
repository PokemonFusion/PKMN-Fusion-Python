def onHit(**bvalues):
	"""function (target, source) {
			var item = target.getItem();
			if (source.hp && item.isBerry && target.takeItem(source)) {
				this.add('-enditem', target, item.name, '[from] stealeat', '[move] Bug Bite', '[of] ' + source);
				if (this.singleEvent('Eat', item, null, source, null, null)) {
					this.runEvent('EatItem', source, null, null, item);
					if (item.id === 'leppaberry')
						target.staleness = 'external';
				}
				if (item.onEat)
					source.ateBerry = true;
			}
		}
	"""
	target = bvalues['target']
	item = target.getItem()


	pass
