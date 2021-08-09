def onBeforeMove(**bvalues):
	"""function (pokemon, target, move) {
				if (!move.isZ && !move.isMax && move.flags['sound']) {
					this.add('cant', pokemon, 'move: Throat Chop');
					return false;
				}
			}
	""" 
	pass

def onDisableMove(**bvalues):
	"""function (pokemon) {
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					if (this.dex.moves.get(moveSlot.id).flags['sound']) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'Throat Chop', '[silent]');
			}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, pokemon, target) {
				if (!move.isZ && !move.isMax && move.flags['sound']) {
					this.add('cant', pokemon, 'move: Throat Chop');
					return false;
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'Throat Chop', '[silent]');
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (target) {
				target.addVolatile('throatchop');
			}
	""" 
	pass
