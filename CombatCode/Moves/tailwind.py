def durationCallback(**bvalues):
	"""function (target, source, effect) {
				if (source && source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 6;
				}
				return 4;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'move: Tailwind');
			}
	""" 
	pass

def onModifySpe(**bvalues):
	"""function (spe, pokemon) {
				return this.chainModify(2);
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (side) {
				this.add('-sideend', side, 'move: Tailwind');
			}
	""" 
	pass
