def onPrepareHit(**bvalues):
	"""function (source, target, move) {
			if (['iceball', 'rollout'].includes(move.id)) return;
			if (move.category !== 'Status' && !move.selfdestruct && !move.multihit && !move.flags['charge'] && !move.spreadHit && !move.isZ) {
				move.multihit = 2;
				move.multihitType = 'parentalbond';
			}
		}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, pokemon, target, move) {
			if (move.multihitType === 'parentalbond' && move.hit > 1) return this.chainModify(0.25);
		}
	""" 
	pass

def onSourceModifySecondaries(**bvalues):
	"""function (secondaries, target, source, move) {
			if (move.multihitType === 'parentalbond' && move.id === 'secretpower' && move.hit < 2) {
				// hack to prevent accidentally suppressing King's Rock/Razor Fang
				return secondaries.filter(effect => effect.volatileStatus === 'flinch');
			}
		}
	""" 
	pass
