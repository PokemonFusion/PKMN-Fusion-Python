def onSourceAccuracy(**bvalues):
	"""function (accuracy, target, source, move) {
				if (move && source === this.effectState.target && target === this.effectState.source)
					return true;
			}
	""" 
	pass

def onSourceInvulnerability(**bvalues):
	"""function (target, source, move) {
				if (move && source === this.effectState.target && target === this.effectState.source)
					return 0;
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source) {
			source.addVolatile('lockon', target);
			this.add('-activate', source, 'move: Lock-On', '[of] ' + target);
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source) {
			if (source.volatiles['lockon'])
				return false;
		}
	""" 
	pass
