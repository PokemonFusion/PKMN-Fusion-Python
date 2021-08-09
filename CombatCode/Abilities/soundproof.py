def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (target !== source && move.flags['sound']) {
				this.add('-immune', target, '[from] ability: Soundproof');
				return null;
			}
		}
	""" 
	pass

def onAllyTryHitSide(**bvalues):
	"""function (target, source, move) {
			if (move.flags['sound']) {
				this.add('-immune', this.effectState.target, '[from] ability: Soundproof');
			}
		}
	""" 
	pass
