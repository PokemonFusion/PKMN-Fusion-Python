def onAfterSubDamage(**bvalues):
	"""function (damage, target, source, move) {
			for (var _i = 0, _a = target.adjacentAllies(); _i < _a.length; _i++) {
				var ally = _a[_i];
				this.damage(ally.baseMaxhp / 16, ally, source, this.dex.conditions.get('Flame Burst'));
			}
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
			for (var _i = 0, _a = target.adjacentAllies(); _i < _a.length; _i++) {
				var ally = _a[_i];
				this.damage(ally.baseMaxhp / 16, ally, source, this.dex.conditions.get('Flame Burst'));
			}
		}
	""" 
	pass
