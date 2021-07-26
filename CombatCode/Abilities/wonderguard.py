def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (target === source || move.category === 'Status' || move.type === '???' || move.id === 'struggle') return;
			this.debug('Wonder Guard immunity: ' + move.id);
			if (target.runEffectiveness(move) <= 0) {
				this.add('-immune', target, '[from] ability: Wonder Guard');
				return null;
			}
		}
	""" 
	pass
