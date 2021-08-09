def onAfterBoost(**bvalues):
	"""function (boost, target, source, effect) {
			var noAtkChange = boost.atk < 0 && target.boosts['atk'] === -6 && target.itemState.lastAtk === -6;
			var noContraryAtkChange = boost.atk > 0 && target.boosts['atk'] === 6 && target.itemState.lastAtk === 6;
			if (target.boosts['spe'] === 6 || noAtkChange || noContraryAtkChange) {
				return;
			}
			if (effect.id === 'intimidate') {
				target.useItem();
			}
		}
	""" 
	pass

def onBoost(**bvalues):
	"""function (boost, target) {
			target.itemState.lastAtk = target.boosts['atk'];
		}
	""" 
	pass
