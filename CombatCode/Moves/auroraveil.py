def durationCallback(**bvalues):
	"""function (target, source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasItem('lightclay')) {
					return 8;
				}
				return 5;
			}
	""" 
	pass

def onAnyModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
				if (target !== source && this.effectState.target.hasAlly(target)) {
					if ((target.side.getSideCondition('reflect') && this.getCategory(move) === 'Physical') ||
						(target.side.getSideCondition('lightscreen') && this.getCategory(move) === 'Special')) {
						return;
					}
					if (!target.getMoveHitData(move).crit && !move.infiltrates) {
						this.debug('Aurora Veil weaken');
						if (this.activePerHalf > 1)
							return this.chainModify([2732, 4096]);
						return this.chainModify(0.5);
					}
				}
			}
	""" 
	pass

def onSideEnd(**bvalues):
	"""function (side) {
				this.add('-sideend', side, 'move: Aurora Veil');
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'move: Aurora Veil');
			}
	""" 
	pass

def onTry(**bvalues):
	"""function () {
			return this.field.isWeather('hail');
			}
	""" 
	pass
