def onModifyType (move, pokemon):
	"""function (move, pokemon) {
			var noModifyType = [
				'hiddenpower', 'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'struggle', 'technoblast', 'terrainpulse', 'weatherball',
			];
			if (!(move.isZ && move.category !== 'Status') && !noModifyType.includes(move.id)) {
				move.type = 'Normal';
				move.normalizeBoosted = True;
			}
		}
	""" 
	pass

def onBasePower (basePower, pokemon, target, move):
	"""function (basePower, pokemon, target, move) {
			if (move.normalizeBoosted)
				return this.chainModify([4915, 4096]);
		}
	""" 
	pass