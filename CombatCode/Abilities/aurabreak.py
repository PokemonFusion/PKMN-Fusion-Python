def onStart (pokemon):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Aura Break');
		}
	""" 
	pass

def onAnyTryPrimaryHit (target, source, move):
	"""function (target, source, move) {
			if (target === source || move.category === 'Status') return;
			move.hasAuraBreak = true;
		}
	""" 
	pass