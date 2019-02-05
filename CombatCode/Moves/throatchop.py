def onStart(datadic : dict):
	"""function (target) {
				this.add('-start', target, 'Throat Chop', '[silent]');
			}
	""" 
	pass

def onDisableMove(datadic : dict):
	"""function (pokemon) {
				for (const moveSlot of pokemon.moveSlots) {
					if (this.getMove(moveSlot.id).flags['sound']) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onBeforeMove(datadic : dict):
	"""function (pokemon, target, move) {
				if (!move.isZ && move.flags['sound']) {
					this.add('cant', pokemon, 'move: Throat Chop');
					return false;
				}
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (target) {
				this.add('-end', target, 'Throat Chop', '[silent]');
			}
	""" 
	pass

def onHit(datadic : dict):
	"""function (target) {
				target.addVolatile('throatchop');
			}
	""" 
	pass
