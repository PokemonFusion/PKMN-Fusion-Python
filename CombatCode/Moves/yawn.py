def onTryHit(datadic : dict):
	"""function (target) {
			if (target.status || !target.runStatusImmunity('slp')) {
				return false;
			}
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target, source) {
				this.add('-start', target, 'move: Yawn', '[of] ' + source);
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (target) {
				this.add('-end', target, 'move: Yawn', '[silent]');
				target.trySetStatus('slp');
			}
	""" 
	pass
