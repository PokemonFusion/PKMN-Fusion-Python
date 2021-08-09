def onModifyType (move, pokemon):
	"""function (move, pokemon) {
			var noModifyType = [
				'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'technoblast', 'terrainpulse', 'weatherball',
			];
			if (move.type === 'Normal' && !noModifyType.includes(move.id) && !(move.isZ && move.category !== 'Status')) {
				move.type = 'Flying';
				move.aerilateBoosted = True;
			}
		}
	""" 
	pass

def onBasePower (basePower, pokemon, target, move):
	"""function (basePower, pokemon, target, move) {
			if (move.aerilateBoosted)
				return this.chainModify([4915, 4096]);
		}
	""" 
	pass