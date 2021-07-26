def onStart(**bvalues):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Comatose');
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Comatose');
			return false;
		}
	""" 
	pass
