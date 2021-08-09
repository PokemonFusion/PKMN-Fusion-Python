def onModifyType(**bvalues):
	"""function (move, pokemon) {
			var noModifyType = [
				'judgment', 'multiattack', 'naturalgift', 'revelationdance', 'technoblast', 'terrainpulse', 'weatherball',
			];
			if (move.type === 'Normal' && !noModifyType.includes(move.id) && !(move.isZ && move.category !== 'Status')) {
				move.type = 'Fairy';
				move.pixilateBoosted = True;
			}
		}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, pokemon, target, move) {
			if (move.pixilateBoosted)
				return this.chainModify([4915, 4096]);
		}
	""" 
	pass
