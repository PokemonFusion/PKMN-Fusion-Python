def onImmunity(datadic : dict):
	"""function (type, pokemon) {
			if (type === 'sandstorm' || type === 'hail' || type === 'powder') return False;
		}
	""" 
	pass

def onTryHit(datadic : dict):
	"""function (pokemon, source, move) {
			if (move.flags['powder'] && pokemon !== source && this.getImmunity('powder', pokemon)) {
				this.add('-activate', pokemon, 'item: Safety Goggles', move.name);
				return null;
			}
		}
	""" 
	pass
