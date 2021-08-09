def onPreStart (pokemon):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Unnerve');
			this.effectState.unnerved = True;
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
			if (this.effectState.unnerved)
				return;
			this.add('-ability', pokemon, 'Unnerve');
			this.effectState.unnerved = True;
		}
	""" 
	pass

def onEnd ():
	"""function () {
			this.effectState.unnerved = False;
		}
	""" 
	pass

def onFoeTryEatItem ():
	"""function () {
			return !this.effectState.unnerved;
		}
	""" 
	pass