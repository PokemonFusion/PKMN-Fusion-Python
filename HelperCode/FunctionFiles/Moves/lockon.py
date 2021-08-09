def onSourceAccuracy (accuracy, target, source, move):
	"""function (accuracy, target, source, move) {
				if (move && source === this.effectState.target && target === this.effectState.source)
					return true;
			}
	""" 
	pass

def onSourceInvulnerability (target, source, move):
	"""function (target, source, move) {
				if (move && source === this.effectState.target && target === this.effectState.source)
					return 0;
			}
	""" 
	pass

def onHit (target, source):
	"""function (target, source) {
			source.addVolatile('lockon', target);
			this.add('-activate', source, 'move: Lock-On', '[of] ' + target);
		}
	""" 
	pass

def onTryHit (target, source):
	"""function (target, source) {
			if (source.volatiles['lockon'])
				return false;
		}
	""" 
	pass