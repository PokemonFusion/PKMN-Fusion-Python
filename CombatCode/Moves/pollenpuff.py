def onHit(**bvalues):
	"""function (target, source) {
			if (source.isAlly(target)) {
				if (!this.heal(Math.floor(target.baseMaxhp * 0.5))) {
					this.add('-immune', target);
				}
			}
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (source.isAlly(target)) {
				move.basePower = 0;
				move.infiltrates = true;
			}
		}
	""" 
	pass
