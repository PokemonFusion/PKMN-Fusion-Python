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
				if (target !== source && this.effectState.target.hasAlly(target) && this.getCategory(move) === 'Physical') {
					if (!target.getMoveHitData(move).crit && !move.infiltrates) {
						this.debug('Reflect weaken');
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
				this.add('-sideend', side, 'Reflect');
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'Reflect');
			}
	""" 
	pass
