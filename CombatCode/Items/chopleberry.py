def onEat(**bvalues):
	"""function () { }
	""" 
	pass

def onSourceModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
			if (move.type === 'Fighting' && target.getMoveHitData(move).typeMod > 0) {
				var hitSub = target.volatiles['substitute'] && !move.flags['authentic'] && !(move.infiltrates && this.gen >= 6);
				if (hitSub)
					return;
				if (target.eatItem()) {
					this.debug('-50% reduction');
					this.add('-enditem', target, this.effect, '[weaken]');
					return this.chainModify(0.5);
				}
			}
		}
	""" 
	pass
