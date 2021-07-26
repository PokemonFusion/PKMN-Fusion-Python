def durationCallback(**bvalues):
	"""function (target, source, effect) {
				if (source && source.hasItem('lightclay')) {
					return 8;
				}
				return 5;
			}
	""" 
	pass

def onAnyModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
				if (target !== source && target.side === this.effectData.target && this.getCategory(move) === 'Physical') {
					if (!move.crit && !move.infiltrates) {
						this.debug('Reflect weaken');
						if (target.side.active.length > 1) return this.chainModify([0xAAC, 0x1000]);
						return this.chainModify(0.5);
					}
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'Reflect');
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (side) {
				this.add('-sideend', side, 'Reflect');
			}
	""" 
	pass
