def onTryHit(datadic : dict):
	"""function (target) {
			if (!target.newlySwitched && !this.willMove(target)) return false;
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target, source) {
				this.effectData.multiplier = 1.5;
				this.add('-singleturn', target, 'Helping Hand', '[of] ' + source);
			}
	""" 
	pass

def onRestart(datadic : dict):
	"""function (target, source) {
				this.effectData.multiplier *= 1.5;
				this.add('-singleturn', target, 'Helping Hand', '[of] ' + source);
			}
	""" 
	pass

def onBasePower(datadic : dict):
	"""function (basePower) {
				this.debug('Boosting from Helping Hand: ' + this.effectData.multiplier);
				return this.chainModify(this.effectData.multiplier);
			}
	""" 
	pass
