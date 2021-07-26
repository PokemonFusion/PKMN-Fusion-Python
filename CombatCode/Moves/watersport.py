def onStart(**bvalues):
	"""function (side, source) {
				this.add('-fieldstart', 'move: Water Sport', '[of] ' + source);
			}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('water sport weaken');
					return this.chainModify([0x548, 0x1000]);
				}
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function () {
				this.add('-fieldend', 'move: Water Sport');
			}
	""" 
	pass
