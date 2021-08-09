def onAnyInvulnerability(**bvalues):
	"""function (target, source, move) {
			if (move && (source === this.effectState.target || target === this.effectState.target))
				return 0;
		}
	""" 
	pass

def onAnyAccuracy(**bvalues):
	"""function (accuracy, target, source, move) {
			if (move && (source === this.effectState.target || target === this.effectState.target)) {
				return True;
			}
			return accuracy;
		}
	""" 
	pass
