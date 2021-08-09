def onEnd (pokemon):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Laser Focus', '[silent]');
			}
	""" 
	pass

def onModifyCritRatio (critRatio):
	"""function (critRatio) {
				return 5;
			}
	""" 
	pass

def onRestart (pokemon):
	"""function (pokemon) {
				this.effectState.duration = 2;
				this.add('-start', pokemon, 'move: Laser Focus');
			}
	""" 
	pass

def onStart (pokemon, source, effect):
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