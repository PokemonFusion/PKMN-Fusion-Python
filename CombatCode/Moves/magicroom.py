def durationCallback(**bvalues):
	"""function (source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onFieldEnd(**bvalues):
	"""function () {
				this.add('-fieldend', 'move: Magic Room', '[of] ' + this.effectState.source);
			}
	""" 
	pass

def onFieldRestart(**bvalues):
	"""function (target, source) {
				this.field.removePseudoWeather('magicroom');
			}
	""" 
	pass

def onFieldStart(**bvalues):
	"""function (target, source) {
				this.add('-fieldstart', 'move: Magic Room', '[of] ' + source);
			}
	""" 
	pass
