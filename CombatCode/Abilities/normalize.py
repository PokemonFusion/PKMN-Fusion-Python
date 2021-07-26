def onModifyMove(**bvalues):
	"""function (move, pokemon) {
			if (!(move.isZ && move.category !== 'Status') && !['hiddenpower', 'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'struggle', 'technoblast', 'weatherball'].includes(move.id)) {
				move.type = 'Normal';
				move.normalizeBoosted = true;
			}
		}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, pokemon, target, move) {
			if (move.normalizeBoosted) return this.chainModify([0x1333, 0x1000]);
		}
	""" 
	pass
