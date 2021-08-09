def onImmunity (type, pokemon):
	"""function (type, pokemon) {
			if (type === 'sandstorm' || type === 'hail' || type === 'powder')
				return False;
		}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
			if (move.flags['powder'] && target !== source && this.dex.getImmunity('powder', target)) {
				this.add('-immune', target, '[from] ability: Overcoat');
				return null;
			}
		}
	""" 
	pass