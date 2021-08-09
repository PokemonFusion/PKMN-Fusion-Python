def onHit (target, source):
	"""function (target, source) {
			if (source.isAlly(target)) {
				if (!this.heal(Math.floor(target.baseMaxhp * 0.5))) {
					this.add('-immune', target);
				}
			}
		}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (source.isAlly(target)) {
				move.basePower = 0;
				move.infiltrates = true;
			}
		}
	""" 
	pass