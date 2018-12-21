def durationCallback (source, effect):
	"""function (source, effect) {
				if (source && source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onStart (target, source):
	"""function (target, source) {
				this.add('-fieldstart', 'move: Magic Room', '[of] ' + source);
			}
	""" 
	pass

def onRestart (target, source):
	"""function (target, source) {
				this.removePseudoWeather('magicroom');
			}
	""" 
	pass

def onEnd ():
	"""function () {
				this.add('-fieldend', 'move: Magic Room', '[of] ' + this.effectData.source);
			}
	""" 
	pass