def onPreStart(**bvalues):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'As One');
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

def onSourceAfterFaint(**bvalues):
	"""function (length, target, source, effect) {
			if (effect && effect.effectType === 'Move') {
				this.boost({ atk: length }, source, source, this.dex.abilities.get('chillingneigh'));
			}
		}
	""" 
	pass
