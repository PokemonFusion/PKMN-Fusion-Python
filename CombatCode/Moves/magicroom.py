def durationCallback(**bvalues):
	"""function (source, effect) {
				if (source && source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source) {
				this.add('-fieldstart', 'move: Magic Room', '[of] ' + source);
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (target, source) {
				this.removePseudoWeather('magicroom');
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function () {
				this.add('-fieldend', 'move: Magic Room', '[of] ' + this.effectData.source);
			}
	""" 
	pass
