def onSwitchIn (pokemon):
	"""function (pokemon) {
			this.effectState.switchingIn = True;
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
			// Air Lock does not activate when Skill Swapped or when Neutralizing Gas leaves the field
			if (!this.effectState.switchingIn)
				return;
			this.add('-ability', pokemon, 'Air Lock');
			this.effectState.switchingIn = False;
		}
	""" 
	pass