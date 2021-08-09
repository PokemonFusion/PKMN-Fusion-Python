def onModifyMove(**bvalues):
	"""function (move, pokemon) {
			if (move.secondaries) {
				delete move.secondaries;
				// Technically not a secondary effect, but it is negated
				delete move.self;
				if (move.id === 'clangoroussoulblaze')
					delete move.selfBoost;
				// Actual negation of AfterMoveSecondary effects implemented in scripts.js
				move.hasSheerForce = True;
			}
		}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, pokemon, target, move) {
			if (move.hasSheerForce)
				return this.chainModify([5325, 4096]);
		}
	""" 
	pass
