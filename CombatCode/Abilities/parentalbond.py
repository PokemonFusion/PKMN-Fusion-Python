def onPrepareHit(**bvalues):
	"""function (source, target, move) {
			if (move.category === 'Status' || move.selfdestruct || move.multihit)
				return;
			if (['endeavor', 'fling', 'iceball', 'rollout'].includes(move.id))
				return;
			if (!move.flags['charge'] && !move.spreadHit && !move.isZ && !move.isMax) {
				move.multihit = 2;
				move.multihitType = 'parentalbond';
			}
		}
	""" 
	pass

def onSourceModifySecondaries(**bvalues):
	"""function (secondaries, target, source, move) {
			if (move.multihitType === 'parentalbond' && move.id === 'secretpower' && move.hit < 2) {
				// hack to prevent accidentally suppressing King's Rock/Razor Fang
				return secondaries.filter(function (effect) { return effect.volatileStatus === 'flinch'; });
			}
		}
	""" 
	pass
