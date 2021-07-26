def onTryHit(**bvalues):
	"""function (target, source) {
			if (source.volatiles['lockon']) return false;
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

def onSourceAccuracy(**bvalues):
	"""function (accuracy, target, source, move) {
				if (move && source === this.effectData.target && target === this.effectData.source) return true;
			}
	""" 
	pass
