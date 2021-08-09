def onTry(**bvalues):
	"""function (source, target, move) {
			// Additional Gravity check for Z-move variant
			if (this.field.getPseudoWeather('Gravity')) {
				this.add('cant', source, 'move: Gravity', move);
				return null;
			}
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source) {
			this.add('-nothing');
		}
	""" 
	pass
