def onBasePower(**bvalues):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('water sport weaken');
					return this.chainModify([1352, 4096]);
				}
			}
	""" 
	pass

def onFieldEnd(**bvalues):
	"""function () {
				this.add('-fieldend', 'move: Water Sport');
			}
	""" 
	pass

def onFieldStart(**bvalues):
	"""function (field, source) {
				this.add('-fieldstart', 'move: Water Sport', '[of] ' + source);
			}
	""" 
	pass
