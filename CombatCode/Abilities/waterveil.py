def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.status === 'brn') {
				this.add('-activate', pokemon, 'ability: Water Veil');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			if (status.id !== 'brn') return;
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Water Veil');
			return false;
		}
	""" 
	pass
