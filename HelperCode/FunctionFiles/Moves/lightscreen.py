def durationCallback (target, source, effect):
	"""function (target, source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasItem('lightclay')) {
					return 8;
				}
				return 5;
			}
	""" 
	pass

def onAnyModifyDamage (damage, source, target, move):
	"""function (damage, source, target, move) {
				if (target !== source && this.effectState.target.hasAlly(target) && this.getCategory(move) === 'Special') {
					if (!target.getMoveHitData(move).crit && !move.infiltrates) {
						this.debug('Light Screen weaken');
						if (this.activePerHalf > 1)
							return this.chainModify([2732, 4096]);
						return this.chainModify(0.5);
					}
				}
			}
	""" 
	pass

def onSideEnd (side):
	"""function (side) {
				this.add('-sideend', side, 'move: Light Screen');
			}
	""" 
	pass

def onSideStart (side):
	"""function (side) {
				this.add('-sidestart', side, 'move: Light Screen');
			}
	""" 
	pass