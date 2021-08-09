def onHit(**bvalues):
	"""function (target, source, move) {
			if (source && source !== target && !source.item && move && this.checkMoveMakesContact(move, source, target)) {
				var barb = target.takeItem();
				if (!barb)
					return; // Gen 4 Multitype
				source.setItem(barb);
				// no message for Sticky Barb changing hands
			}
		}
	""" 
	pass

def onResidual(**bvalues):
	"""function (pokemon) {
			this.damage(pokemon.baseMaxhp / 8);
		}
	""" 
	pass
