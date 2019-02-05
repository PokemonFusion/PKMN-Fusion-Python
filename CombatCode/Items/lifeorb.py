def onModifyDamage(datadic : dict):
	"""function (damage, source, target, move) {
			return this.chainModify([0x14CC, 0x1000]);
		}
	""" 
	pass

def onAfterMoveSecondarySelf(datadic : dict):
	"""function (source, target, move) {
			if (source && source !== target && move && move.category !== 'Status') {
				this.damage(source.maxhp / 10, source, source, this.getItem('lifeorb'));
			}
		}
	""" 
	pass
