def onStart (target):
	"""function (target) {
				if (target.activeTurns && !this.willMove(target)) {
					this.effectData.duration++;
				}
				this.add('-start', target, 'move: Taunt');
			}
	""" 
	pass

def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'move: Taunt');
			}
	""" 
	pass

def onDisableMove (pokemon):
	"""function (pokemon) {
				for (const moveSlot of pokemon.moveSlots) {
					if (this.getMove(moveSlot.id).category === 'Status') {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onBeforeMove (attacker, defender, move):
	"""function (attacker, defender, move) {
				if (!move.isZ && move.category === 'Status') {
					this.add('cant', attacker, 'move: Taunt', move);
					return false;
				}
			}
	""" 
	pass