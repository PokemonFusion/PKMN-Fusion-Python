def onStart(**bvalues):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Comatose');
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			var _a;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				this.add('-immune', target, '[from] ability: Comatose');
			}
			return False;
		}
	""" 
	pass
