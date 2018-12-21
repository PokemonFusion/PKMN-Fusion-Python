def durationCallback (target, source, effect):
	"""function (target, source, effect) {
				if (source && source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 6;
				}
				return 4;
			}
	""" 
	pass

def onStart (side):
	"""function (side) {
				this.add('-sidestart', side, 'move: Tailwind');
			}
	""" 
	pass

def onModifySpe (spe, pokemon):
	"""function (spe, pokemon) {
				return this.chainModify(2);
			}
	""" 
	pass

def onEnd (side):
	"""function (side) {
				this.add('-sideend', side, 'move: Tailwind');
			}
	""" 
	pass