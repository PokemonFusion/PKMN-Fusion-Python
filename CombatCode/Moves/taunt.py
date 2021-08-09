def onBeforeMove(**bvalues):
	"""function (attacker, defender, move) {
				if (!move.isZ && !move.isMax && move.category === 'Status' && move.id !== 'mefirst') {
					this.add('cant', attacker, 'move: Taunt', move);
					return false;
				}
			}
	""" 
	pass

def onDisableMove(**bvalues):
	"""function (pokemon) {
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					var move = this.dex.moves.get(moveSlot.id);
					if (move.category === 'Status' && move.id !== 'mefirst') {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'move: Taunt');
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				if (target.activeTurns && !this.queue.willMove(target)) {
					this.effectState.duration++;
				}
				this.add('-start', target, 'move: Taunt');
			}
	""" 
	pass
