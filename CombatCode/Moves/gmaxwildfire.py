def onResidual(**bvalues):
	"""function (target) {
				if (!target.hasType('Fire'))
					this.damage(target.baseMaxhp / 6, target);
			}
	""" 
	pass

def onSideEnd(**bvalues):
	"""function (targetSide) {
				this.add('-sideend', targetSide, 'G-Max Wildfire');
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (targetSide) {
				this.add('-sidestart', targetSide, 'G-Max Wildfire');
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (source) {
				for (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {
					var side = _a[_i];
					side.addSideCondition('gmaxwildfire');
				}
			}
	""" 
	pass
