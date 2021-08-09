def onImmunity(**bvalues):
	"""function (type, pokemon) {
			if (type === 'sandstorm' || type === 'hail' || type === 'powder')
				return false;
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (pokemon, source, move) {
			if (move.flags['powder'] && pokemon !== source && this.dex.getImmunity('powder', pokemon)) {
				this.add('-activate', pokemon, 'item: Safety Goggles', move.name);
				return null;
			}
		}
	""" 
	pass
