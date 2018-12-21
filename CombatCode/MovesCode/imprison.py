def onStart (target):
	"""function (target) {
				this.add('-start', target, 'move: Imprison');
			}
	""" 
	pass

def onFoeDisableMove (pokemon):
	"""function (pokemon) {
				for (const moveSlot of this.effectData.source.moveSlots) {
					if (moveSlot.id === 'struggle') continue;
					pokemon.disableMove(moveSlot.id, 'hidden');
				}
				pokemon.maybeDisabled = true;
			}
	""" 
	pass

def onFoeBeforeMove (attacker, defender, move):
	"""function (attacker, defender, move) {
				if (move.id !== 'struggle' && this.effectData.source.hasMove(move.id) && !move.isZ) {
					this.add('cant', attacker, 'move: Imprison', move);
					return false;
				}
			}
	""" 
	pass