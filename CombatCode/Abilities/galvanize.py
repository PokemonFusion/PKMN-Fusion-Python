def onModifyMove(**bvalues):
	"""function (move, pokemon) {
			if (move.type === 'Normal' && !['judgment', 'multiattack', 'naturalgift', 'revelationdance', 'technoblast', 'weatherball'].includes(move.id) && !(move.isZ && move.category !== 'Status')) {
				move.type = 'Electric';
				move.galvanizeBoosted = true;
			}
		}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, pokemon, target, move) {
			if (move.galvanizeBoosted) return this.chainModify([0x1333, 0x1000]);
		}
	""" 
	pass
