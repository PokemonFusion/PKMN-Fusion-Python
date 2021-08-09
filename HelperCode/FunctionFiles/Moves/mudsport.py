def onBasePower (basePower, attacker, defender, move):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Electric') {
					this.debug('mud sport weaken');
					return this.chainModify([1352, 4096]);
				}
			}
	""" 
	pass

def onFieldEnd ():
	"""function () {
				this.add('-fieldend', 'move: Mud Sport');
			}
	""" 
	pass

def onFieldStart (field, source):
	"""function (field, source) {
				this.add('-fieldstart', 'move: Mud Sport', '[of] ' + source);
			}
	""" 
	pass