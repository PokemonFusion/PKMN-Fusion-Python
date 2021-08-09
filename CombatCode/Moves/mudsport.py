def onBasePower(**bvalues):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Electric') {
					this.debug('mud sport weaken');
					return this.chainModify([1352, 4096]);
				}
			}
	""" 
	pass

def onFieldEnd(**bvalues):
	"""function () {
				this.add('-fieldend', 'move: Mud Sport');
			}
	""" 
	pass

def onFieldStart(**bvalues):
	"""function (field, source) {
				this.add('-fieldstart', 'move: Mud Sport', '[of] ' + source);
			}
	""" 
	pass
