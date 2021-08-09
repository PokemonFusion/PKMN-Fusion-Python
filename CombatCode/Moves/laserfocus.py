def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Laser Focus', '[silent]');
			}
	""" 
	pass

def onModifyCritRatio(**bvalues):
	"""function (critRatio) {
				return 5;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (pokemon) {
				this.effectState.duration = 2;
				this.add('-start', pokemon, 'move: Laser Focus');
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon, source, effect) {
				if (effect && (['imposter', 'psychup', 'transform'].includes(effect.id))) {
					this.add('-start', pokemon, 'move: Laser Focus', '[silent]');
				}
				else {
					this.add('-start', pokemon, 'move: Laser Focus');
				}
			}
	""" 
	pass
