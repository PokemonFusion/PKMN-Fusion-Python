def durationCallback (source, effect):
	"""function (source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onFieldEnd ():
	"""function () {
				this.add('-fieldend', 'move: Wonder Room');
			}
	""" 
	pass

def onFieldRestart (target, source):
	"""function (target, source) {
				this.field.removePseudoWeather('wonderroom');
			}
	""" 
	pass

def onFieldStart (field, source):
	"""function (field, source) {
				this.add('-fieldstart', 'move: Wonder Room', '[of] ' + source);
			}
	""" 
	pass