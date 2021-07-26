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
			if (status.id !== 'brn') return;
			if (!effect || !effect.status) return false;
			this.add('-immune', target, '[from] ability: Water Bubble');
			return false;
		}
	""" 
	pass
