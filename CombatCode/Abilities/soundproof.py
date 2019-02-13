def onTryHit(datadic : dict):
	"""function (target, source, move) {
			if (move.flags['sound']) {
				this.add('-immune', target, '[from] ability: Soundproof');
				return null;
			}
		}
	""" 
	pass

def onAllyTryHitSide(datadic : dict):
	"""function (target, source, move) {
			if (move.flags['sound']) {
				this.add('-immune', this.effectData.target, '[from] ability: Soundproof');
			}
		}
	""" 
	pass
