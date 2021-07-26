def onTryHit(**bvalues):
	"""function (target, source) {
			if (source.volatiles['lockon']) return false;
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source) {
			source.addVolatile('lockon', target);
			this.add('-activate', source, 'move: Mind Reader', '[of] ' + target);
		}
	""" 
	pass
