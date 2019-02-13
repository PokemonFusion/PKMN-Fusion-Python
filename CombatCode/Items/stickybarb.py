def onResidual(datadic : dict):
	"""function (pokemon) {
			this.damage(pokemon.maxhp / 8);
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (target, source, move) {
			if (source && source !== target && !source.item && move && move.flags['contact']) {
				let barb = target.takeItem();
				if (!barb) return; // Gen 4 Multitype
				source.setItem(barb);
				// no message for Sticky Barb changing hands
			}
		}
	""" 
	pass
