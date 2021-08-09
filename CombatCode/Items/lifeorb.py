def onAfterMoveSecondarySelf(**bvalues):
	"""function (source, target, move) {
			if (source && source !== target && move && move.category !== 'Status') {
				this.damage(source.baseMaxhp / 10, source, source, this.dex.items.get('lifeorb'));
			}
		}
	""" 
	pass

def onModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
			return this.chainModify([5324, 4096]);
		}
	""" 
	pass
