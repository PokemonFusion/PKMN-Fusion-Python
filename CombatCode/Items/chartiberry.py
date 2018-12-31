def onSourceModifyDamage (damage, source, target, move):
	"""function (damage, source, target, move) {
			if (move.type === 'Rock' && move.typeMod > 0 && (!target.volatiles['substitute'] || move.flags['authentic'] || (move.infiltrates && this.gen >= 6))) {
				if (target.eatItem()) {
					this.debug('-50% reduction');
					this.add('-enditem', target, this.effect, '[weaken]');
					return this.chainModify(0.5);
				}
			}
		}
	""" 
	pass