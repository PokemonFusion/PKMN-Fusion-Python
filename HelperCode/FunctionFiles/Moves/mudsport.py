def onStart (side, source):
	"""function (side, source) {
				this.add('-fieldstart', 'move: Mud Sport', '[of] ' + source);
			}
	""" 
	pass

def onBasePower (basePower, attacker, defender, move):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Electric') {
					this.debug('mud sport weaken');
					return this.chainModify([0x548, 0x1000]);
				}
			}
	""" 
	pass

def onEnd ():
	"""function () {
				this.add('-fieldend', 'move: Mud Sport');
			}
	""" 
	pass