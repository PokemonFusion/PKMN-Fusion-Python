def onBeforeMove (pokemon, target, move):
	"""function (pokemon, target, move) {
				if (!move.isZ && !move.isMax && move.flags['sound']) {
					this.add('cant', pokemon, 'move: Throat Chop');
					return false;
				}
			}
	""" 
	pass

def onDisableMove (pokemon):
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

def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'Throat Chop', '[silent]');
			}
	""" 
	pass

def onModifyMove (move, pokemon, target):
	"""function (move, pokemon, target) {
				if (!move.isZ && !move.isMax && move.flags['sound']) {
					this.add('cant', pokemon, 'move: Throat Chop');
					return false;
				}
			}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-start', target, 'Throat Chop', '[silent]');
			}
	""" 
	pass

def onHit (target):
	"""function (target) {
				target.addVolatile('throatchop');
			}
	""" 
	pass