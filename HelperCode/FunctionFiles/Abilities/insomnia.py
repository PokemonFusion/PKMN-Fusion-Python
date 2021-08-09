def onUpdate (pokemon):
	"""function (pokemon) {
			if (pokemon.status === 'slp') {
				this.add('-activate', pokemon, 'ability: Insomnia');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			var _a;
			if (status.id !== 'slp')
				return;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				this.add('-immune', target, '[from] ability: Insomnia');
			}
			return False;
		}
	""" 
	pass