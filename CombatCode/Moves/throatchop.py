def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'Throat Chop', '[silent]');
			}
	""" 
	pass

def onDisableMove(**bvalues):
	"""function (pokemon) {
				for (const moveSlot of pokemon.moveSlots) {
					if (this.getMove(moveSlot.id).flags['sound']) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onBeforeMove(**bvalues):
	"""function (pokemon, target, move) {
				if (!move.isZ && move.flags['sound']) {
					this.add('cant', pokemon, 'move: Throat Chop');
					return false;
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

def onHit(**bvalues):
	"""function (target) {
				target.addVolatile('throatchop');
			}
	""" 
	pass
