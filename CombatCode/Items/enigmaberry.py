def onEat(**bvalues):
	"""function () { }
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
			if (move && target.getMoveHitData(move).typeMod > 0) {
				if (target.eatItem()) {
					this.heal(target.baseMaxhp / 4);
				}
			}
		}
	""" 
	pass

def onTryEatItem(**bvalues):
	"""function (item, pokemon) {
			if (!this.runEvent('TryHeal', pokemon))
				return false;
		}
	""" 
	pass
