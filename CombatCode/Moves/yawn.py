def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'move: Yawn', '[silent]');
				target.trySetStatus('slp', this.effectState.source);
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source) {
				this.add('-start', target, 'move: Yawn', '[of] ' + source);
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (target.status || !target.runStatusImmunity('slp')) {
				return false;
			}
		}
	""" 
	pass
