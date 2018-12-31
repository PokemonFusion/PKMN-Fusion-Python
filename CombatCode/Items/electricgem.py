def onSourceTryPrimaryHit (target, source, move):
	"""function (target, source, move) {
			if (target === source || move.category === 'Status' || ['firepledge', 'grasspledge', 'waterpledge'].includes(move.id)) return;
			if (move.type === 'Electric') {
				if (source.useItem()) {
					this.add('-enditem', source, 'Electric Gem', '[from] gem', '[move] ' + move.name);
					source.addVolatile('gem');
				}
			}
		}
	""" 
	pass