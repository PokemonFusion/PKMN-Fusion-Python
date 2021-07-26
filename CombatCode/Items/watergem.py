def onSourceTryPrimaryHit(**bvalues):
	"""function (target, source, move) {
			if (target === source || move.category === 'Status' || ['firepledge', 'grasspledge', 'waterpledge'].includes(move.id)) return;
			if (move.type === 'Water') {
				if (source.useItem()) {
					this.add('-enditem', source, 'Water Gem', '[from] gem', '[move] ' + move.name);
					source.addVolatile('gem');
				}
			}
		}
	""" 
	pass
