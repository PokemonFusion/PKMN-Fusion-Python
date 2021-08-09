def onDisableMove (pokemon):
	"""function (pokemon) {
				if (!this.effectState.move || !pokemon.hasMove(this.effectState.move)) {
					return;
				}
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					if (moveSlot.id !== this.effectState.move) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'Encore');
			}
	""" 
	pass

def onOverrideAction (pokemon, target, move):
	"""function (pokemon, target, move) {
				if (move.id !== this.effectState.move)
					return this.effectState.move;
			}
	""" 
	pass

def onResidual (target):
	"""function (target) {
				if (target.moves.includes(this.effectState.move) &&
					target.moveSlots[target.moves.indexOf(this.effectState.move)].pp <= 0) {
					// early termination if you run out of PP
					target.removeVolatile('encore');
				}
			}
	""" 
	pass

def onStart (target):
	"""function (target) {
				var noEncore = [
					'assist', 'copycat', 'encore', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'sketch', 'sleeptalk', 'struggle', 'transform',
				];
				var move = target.lastMove;
				if (!move || target.volatiles['dynamax'])
					return false;
				if (move.isMax && move.baseMove)
					move = this.dex.moves.get(move.baseMove);
				var moveIndex = target.moves.indexOf(move.id);
				if (move.isZ || noEncore.includes(move.id) || !target.moveSlots[moveIndex] || target.moveSlots[moveIndex].pp <= 0) {
					// it failed
					return false;
				}
				this.effectState.move = move.id;
				this.add('-start', target, 'Encore');
				if (!this.queue.willMove(target)) {
					this.effectState.duration++;
				}
			}
	""" 
	pass