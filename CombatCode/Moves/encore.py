def onStart(datadic : dict):
	"""function (target) {
				let noEncore = ['assist', 'copycat', 'encore', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'sketch', 'sleeptalk', 'struggle', 'transform'];
				let moveIndex = target.lastMove ? target.moves.indexOf(target.lastMove.id) : -1;
				if (!target.lastMove || target.lastMove.isZ || noEncore.includes(target.lastMove.id) || !target.moveSlots[moveIndex] || target.moveSlots[moveIndex].pp <= 0) {
					// it failed
					delete target.volatiles['encore'];
					return false;
				}
				this.effectData.move = target.lastMove.id;
				this.add('-start', target, 'Encore');
				if (!this.willMove(target)) {
					this.effectData.duration++;
				}
			}
	""" 
	pass

def onOverrideAction(datadic : dict):
	"""function (pokemon, target, move) {
				if (move.id !== this.effectData.move) return this.effectData.move;
			}
	""" 
	pass

def onResidual(datadic : dict):
	"""function (target) {
				if (target.moves.includes(this.effectData.move) && target.moveSlots[target.moves.indexOf(this.effectData.move)].pp <= 0) { // early termination if you run out of PP
					delete target.volatiles.encore;
					this.add('-end', target, 'Encore');
				}
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (target) {
				this.add('-end', target, 'Encore');
			}
	""" 
	pass

def onDisableMove(datadic : dict):
	"""function (pokemon) {
				if (!this.effectData.move || !pokemon.hasMove(this.effectData.move)) {
					return;
				}
				for (const moveSlot of pokemon.moveSlots) {
					if (moveSlot.id !== this.effectData.move) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass
