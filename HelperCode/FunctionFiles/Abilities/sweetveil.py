def onAllySetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			if (status.id === 'slp') {
				this.debug('Sweet Veil interrupts sleep');
				var effectHolder = this.effectState.target;
				this.add('-block', target, 'ability: Sweet Veil', '[of] ' + effectHolder);
				return null;
			}
		}
	""" 
	pass

def onAllyTryAddVolatile (status, target):
	"""function (status, target) {
			if (status.id === 'yawn') {
				this.debug('Sweet Veil blocking yawn');
				var effectHolder = this.effectState.target;
				this.add('-block', target, 'ability: Sweet Veil', '[of] ' + effectHolder);
				return null;
			}
		}
	""" 
	pass