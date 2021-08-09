def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'Magnet Rise');
			}
	""" 
	pass

def onImmunity(**bvalues):
	"""function (type) {
				if (type === 'Ground')
					return false;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'Magnet Rise');
			}
	""" 
	pass

def onTry(**bvalues):
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
