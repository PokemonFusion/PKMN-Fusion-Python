def onSourceModifyAtk(**bvalues):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Fire') {
				return this.chainModify(0.5);
			}
		}
	""" 
	pass

def onSourceModifySpA(**bvalues):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Fire') {
				return this.chainModify(0.5);
			}
		}
	""" 
	pass

def onModifyAtk(**bvalues):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Water') {
				return this.chainModify(2);
			}
		}
	""" 
	pass

def onModifySpA(**bvalues):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Water') {
				return this.chainModify(2);
			}
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.status === 'brn') {
				this.add('-activate', pokemon, 'ability: Water Bubble');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			var _a;
			if (status.id !== 'brn')
				return;
			if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
				this.add('-immune', target, '[from] ability: Water Bubble');
			}
			return False;
		}
	""" 
	pass
