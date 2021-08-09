def onSourceModifyAtk (atk, attacker, defender, move):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Fire') {
				return this.chainModify(0.5);
			}
		}
	""" 
	pass

def onSourceModifySpA (atk, attacker, defender, move):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Fire') {
				return this.chainModify(0.5);
			}
		}
	""" 
	pass

def onModifyAtk (atk, attacker, defender, move):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Water') {
				return this.chainModify(2);
			}
		}
	""" 
	pass

def onModifySpA (atk, attacker, defender, move):
	"""function (atk, attacker, defender, move) {
			if (move.type === 'Water') {
				return this.chainModify(2);
			}
		}
	""" 
	pass

def onUpdate (pokemon):
	"""function (pokemon) {
			if (pokemon.status === 'brn') {
				this.add('-activate', pokemon, 'ability: Water Bubble');
				pokemon.cureStatus();
			}
		}
	""" 
	pass

def onSetStatus (status, target, source, effect):
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