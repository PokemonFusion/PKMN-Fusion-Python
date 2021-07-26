def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.status === 'slp') {
				this.add('-activate', pokemon, 'ability: Insomnia');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			if (status.id !== 'slp') return;
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Insomnia');
			return false;
		}
	""" 
	pass
