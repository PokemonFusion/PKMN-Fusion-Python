def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.status === 'psn' || pokemon.status === 'tox') {
				this.add('-activate', pokemon, 'ability: Immunity');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			var _a;
			if (status.id !== 'psn' && status.id !== 'tox')
				return;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				this.add('-immune', target, '[from] ability: Immunity');
			}
			return False;
		}
	""" 
	pass
