def onStart (pokemon):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Comatose');
		}
	""" 
	pass

def onSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Comatose');
			return false;
		}
	""" 
	pass