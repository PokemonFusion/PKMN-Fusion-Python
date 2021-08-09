def onFoeBeforeMove(**bvalues):
	"""function (attacker, defender, move) {
				if (move.id !== 'struggle' && this.effectState.source.hasMove(move.id) && !move.isZ && !move.isMax) {
					this.add('cant', attacker, 'move: Imprison', move);
					return false;
				}
			}
	""" 
	pass

def onFoeDisableMove(**bvalues):
	"""function (pokemon) {
				for (var _i = 0, _a = this.effectState.source.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					if (moveSlot.id === 'struggle')
						continue;
					pokemon.disableMove(moveSlot.id, 'hidden');
				}
				pokemon.maybeDisabled = true;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'move: Imprison');
			}
	""" 
	pass
