def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (target === source || move.category === 'Status' || move.type === '???' || move.id === 'struggle')
				return;
			if (move.id === 'skydrop' && !source.volatiles['skydrop'])
				return;
			this.debug('Wonder Guard immunity: ' + move.id);
			if (target.runEffectiveness(move) <= 0) {
				if (move.smartTarget) {
					move.smartTarget = False;
				}
				else {
					this.add('-immune', target, '[from] ability: Wonder Guard');
				}
				return null;
			}
		}
	""" 
	pass