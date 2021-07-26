def onImmunity(**bvalues):
	"""function (type, pokemon) {
			if (type === 'sandstorm' || type === 'hail' || type === 'powder') return False;
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (pokemon, source, move) {
			if (move.flags['powder'] && pokemon !== source && this.getImmunity('powder', pokemon)) {
				this.add('-activate', pokemon, 'item: Safety Goggles', move.name);
				return null;
			}
		}
	""" 
	pass
