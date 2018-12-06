def onUpdate (pokemon):
	"""function (pokemon) {
			if (pokemon.status === 'par') {
				this.add('-activate', pokemon, 'ability: Limber');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			if (status.id !== 'par') return;
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Limber');
			return false;
		}
	""" 
	pass