def durationCallback(datadic : dict):
	"""function (target, source, effect) {
				if (source && source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 6;
				}
				return 4;
			}
	""" 
	pass

def onStart(datadic : dict):
	"""function (side) {
				this.add('-sidestart', side, 'move: Tailwind');
			}
	""" 
	pass

def onModifySpe(datadic : dict):
	"""function (spe, pokemon) {
				return this.chainModify(2);
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (side) {
				this.add('-sideend', side, 'move: Tailwind');
			}
	""" 
	pass
