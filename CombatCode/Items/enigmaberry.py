def onHit(datadic : dict):
	"""function (target, source, move) {
			if (move && move.typeMod > 0) {
				if (target.eatItem()) {
					this.heal(target.maxhp / 4);
				}
			}
		}
	""" 
	pass

def onTryEatItem(datadic : dict):
	"""function (item, pokemon) {
			if (!this.runEvent('TryHeal', pokemon)) return False;
		}
	""" 
	pass
