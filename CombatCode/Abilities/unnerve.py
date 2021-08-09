def onPreStart(**bvalues):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Unnerve');
			this.effectState.unnerved = True;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
			if (this.effectState.unnerved)
				return;
			this.add('-ability', pokemon, 'Unnerve');
			this.effectState.unnerved = True;
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function () {
			this.effectState.unnerved = False;
		}
	""" 
	pass

def onFoeTryEatItem(**bvalues):
	"""function () {
			return !this.effectState.unnerved;
		}
	""" 
	pass
