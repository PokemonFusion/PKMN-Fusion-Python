def onStart(**bvalues):
	"""function (pokemon) {
			for (var _i = 0, _a = pokemon.alliesAndSelf(); _i < _a.length; _i++) {
				var ally = _a[_i];
				if (['psn', 'tox'].includes(ally.status)) {
					this.add('-activate', pokemon, 'ability: Pastel Veil');
					ally.cureStatus();
				}
			}
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (['psn', 'tox'].includes(pokemon.status)) {
				this.add('-activate', pokemon, 'ability: Pastel Veil');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onAllySwitchIn(**bvalues):
	"""function (pokemon) {
			if (['psn', 'tox'].includes(pokemon.status)) {
				this.add('-activate', this.effectState.target, 'ability: Pastel Veil');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			var _a;
			if (!['psn', 'tox'].includes(status.id))
				return;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				this.add('-immune', target, '[from] ability: Pastel Veil');
			}
			return False;
		}
	""" 
	pass

def onAllySetStatus(**bvalues):
	"""function (status, target, source, effect) {
			var _a;
			if (!['psn', 'tox'].includes(status.id))
				return;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				var effectHolder = this.effectState.target;
				this.add('-block', target, 'ability: Pastel Veil', '[of] ' + effectHolder);
			}
			return False;
		}
	""" 
	pass
