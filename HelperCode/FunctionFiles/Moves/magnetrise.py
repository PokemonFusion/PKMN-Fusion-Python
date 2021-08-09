def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'Magnet Rise');
			}
	""" 
	pass

def onImmunity (type):
	"""function (type) {
				if (type === 'Ground')
					return false;
			}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-start', target, 'Magnet Rise');
			}
	""" 
	pass

def onTry (source, target, move):
	"""function (source, target, move) {
			if (target.volatiles['smackdown'] || target.volatiles['ingrain'])
				return false;
			// Additional Gravity check for Z-move variant
			if (this.field.getPseudoWeather('Gravity')) {
				this.add('cant', source, 'move: Gravity', move);
				return null;
			}
		}
	""" 
	pass