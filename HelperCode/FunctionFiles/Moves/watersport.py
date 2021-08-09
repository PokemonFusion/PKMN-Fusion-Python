def onBasePower (basePower, attacker, defender, move):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('water sport weaken');
					return this.chainModify([1352, 4096]);
				}
			}
	""" 
	pass

def onFieldEnd ():
	"""function () {
				this.add('-fieldend', 'move: Water Sport');
			}
	""" 
	pass

def onFieldStart (field, source):
	"""function (field, source) {
				this.add('-fieldstart', 'move: Water Sport', '[of] ' + source);
			}
	""" 
	pass