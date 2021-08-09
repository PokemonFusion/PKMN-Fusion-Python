def onPrepareHit (source, target, move):
	"""function (source, target, move) {
			if (move.hasBounced || move.sourceEffect === 'snatch')
				return;
			var type = move.type;
			if (type && type !== '???' && source.getTypes().join() !== type) {
				if (!source.setType(type))
					return;
				this.add('-start', source, 'typechange', type, '[from] ability: Protean');
			}
		}
	""" 
	pass