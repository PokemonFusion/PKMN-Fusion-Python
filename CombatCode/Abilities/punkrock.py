def onBasePower(**bvalues):
	"""function (basePower, attacker, defender, move) {
			if (move.flags['sound']) {
				this.debug('Punk Rock boost');
				return this.chainModify([5325, 4096]);
			}
		}
	""" 
	pass

def onSourceModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
			if (move.flags['sound']) {
				this.debug('Punk Rock weaken');
				return this.chainModify(0.5);
			}
		}
	""" 
	pass
