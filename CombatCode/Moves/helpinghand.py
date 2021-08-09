def onBasePower(**bvalues):
	"""function (basePower) {
				this.debug('Boosting from Helping Hand: ' + this.effectState.multiplier);
				return this.chainModify(this.effectState.multiplier);
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (target, source) {
				this.effectState.multiplier *= 1.5;
				this.add('-singleturn', target, 'Helping Hand', '[of] ' + source);
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source) {
				this.effectState.multiplier = 1.5;
				this.add('-singleturn', target, 'Helping Hand', '[of] ' + source);
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (!target.newlySwitched && !this.queue.willMove(target))
				return false;
		}
	""" 
	pass
