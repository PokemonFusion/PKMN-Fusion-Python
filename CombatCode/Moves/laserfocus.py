def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-start', pokemon, 'move: Laser Focus');
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (pokemon) {
				this.effectData.duration = 2;
				this.add('-start', pokemon, 'move: Laser Focus');
			}
	""" 
	pass

def onModifyCritRatio(**bvalues):
	"""function (critRatio) {
				return 5;
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Laser Focus', '[silent]');
			}
	""" 
	pass
