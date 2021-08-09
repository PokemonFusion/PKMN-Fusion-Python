def onStart(**bvalues):
	"""function (pokemon) {
			if (this.suppressingAbility(pokemon))
				return;
			this.add('-ability', pokemon, 'Aura Break');
		}
	""" 
	pass

def onAnyTryPrimaryHit(**bvalues):
	"""function (target, source, move) {
			if (target === source || move.category === 'Status')
				return;
			move.hasAuraBreak = True;
		}
	""" 
	pass
