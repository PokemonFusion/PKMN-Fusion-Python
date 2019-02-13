def onStart(datadic : dict):
	"""function (side, source) {
				this.add('-fieldstart', 'move: Water Sport', '[of] ' + source);
			}
	""" 
	pass

def onBasePower(datadic : dict):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('water sport weaken');
					return this.chainModify([0x548, 0x1000]);
				}
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function () {
				this.add('-fieldend', 'move: Water Sport');
			}
	""" 
	pass
