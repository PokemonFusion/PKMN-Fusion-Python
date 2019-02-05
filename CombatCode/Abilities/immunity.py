def onUpdate(datadic : dict):
	"""function (pokemon) {
			if (pokemon.status === 'psn' || pokemon.status === 'tox') {
				this.add('-activate', pokemon, 'ability: Immunity');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus(datadic : dict):
	"""function (status, target, source, effect) {
			if (status.id !== 'psn' && status.id !== 'tox') return;
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Immunity');
			return false;
		}
	""" 
	pass
