def onStart(**bvalues):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Fairy Aura');
		}
	""" 
	pass

def onAnyBasePower(**bvalues):
	"""function (basePower, source, target, move) {
			if (target === source || move.category === 'Status' || move.type !== 'Fairy') return;
			if (!move.auraBooster) move.auraBooster = this.effectData.target;
			if (move.auraBooster !== this.effectData.target) return;
			return this.chainModify([move.hasAuraBreak ? 0x0C00 : 0x1547, 0x1000]);
		}
	""" 
	pass
