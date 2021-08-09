def onModifyType(**bvalues):
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

def onBasePower(**bvalues):
	"""function (basePower, pokemon, target, move) {
			if (move.normalizeBoosted)
				return this.chainModify([4915, 4096]);
		}
	""" 
	pass
