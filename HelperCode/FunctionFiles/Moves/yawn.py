def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'move: Yawn', '[silent]');
				target.trySetStatus('slp', this.effectState.source);
			}
	""" 
	pass

def onStart (target, source):
	"""function (target, source) {
				this.add('-start', target, 'move: Yawn', '[of] ' + source);
			}
	""" 
	pass

def onTryHit (target):
	"""function (target) {
			if (target.status || !target.runStatusImmunity('slp')) {
				return false;
			}
		}
	""" 
	pass