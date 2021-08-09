def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.status === 'par') {
				this.add('-activate', pokemon, 'ability: Limber');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			var _a;
			if (status.id !== 'par')
				return;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				this.add('-immune', target, '[from] ability: Limber');
			}
			return False;
		}
	""" 
	pass
