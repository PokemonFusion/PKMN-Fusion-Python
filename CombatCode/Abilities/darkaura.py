def onStart(**bvalues):
	"""function (pokemon) {
			if (this.suppressingAbility(pokemon))
				return;
			this.add('-ability', pokemon, 'Dark Aura');
		}
	""" 
	pass

def onAnyBasePower(**bvalues):
	"""function (basePower, source, target, move) {
			if (target === source || move.category === 'Status' || move.type !== 'Dark')
				return;
			if (!move.auraBooster)
				move.auraBooster = this.effectState.target;
			if (move.auraBooster !== this.effectState.target)
				return;
			return this.chainModify([move.hasAuraBreak ? 3072 : 5448, 4096]);
		}
	""" 
	pass
