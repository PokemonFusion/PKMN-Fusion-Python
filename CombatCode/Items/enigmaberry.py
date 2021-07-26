def onHit(**bvalues):
	"""function (target, source, move) {
			if (move && move.typeMod > 0) {
				if (target.eatItem()) {
					this.heal(target.maxhp / 4);
				}
			}
		}
	""" 
	pass

def onTryEatItem(**bvalues):
	"""function (item, pokemon) {
			if (!this.runEvent('TryHeal', pokemon)) return False;
		}
	""" 
	pass
