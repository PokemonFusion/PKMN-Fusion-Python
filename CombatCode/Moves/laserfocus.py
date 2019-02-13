def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-start', pokemon, 'move: Laser Focus');
			}
	""" 
	pass

def onRestart(datadic : dict):
	"""function (pokemon) {
				this.effectData.duration = 2;
				this.add('-start', pokemon, 'move: Laser Focus');
			}
	""" 
	pass

def onModifyCritRatio(datadic : dict):
	"""function (critRatio) {
				return 5;
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Laser Focus', '[silent]');
			}
	""" 
	pass
