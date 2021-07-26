def onAllySetStatus(**bvalues):
	"""function (status, target, source, effect) {
			if (status.id === 'slp') {
				this.debug('Sweet Veil interrupts sleep');
				this.add('-activate', this.effectData.target, 'ability: Sweet Veil', '[of] ' + target);
				return null;
			}
		}
	""" 
	pass

def onAllyTryAddVolatile(**bvalues):
	"""function (status, target) {
			if (status.id === 'yawn') {
				this.debug('Sweet Veil blocking yawn');
				this.add('-activate', this.effectData.target, 'ability: Sweet Veil', '[of] ' + target);
				return null;
			}
		}
	""" 
	pass
