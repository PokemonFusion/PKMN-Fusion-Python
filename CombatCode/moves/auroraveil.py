def onTryHitSide():
    # function () {
	# 		if (!this.isWeather('hail')) return False;
	# 	}
    pass

def durationCallback(target, source, effect):
    # function (target, source, effect) {
	# 			if (source && source.hasItem('lightclay')) {
	# 				return 8;
	# 			}
	# 			return 5;
	# 		}
    pass

def onAnyModifyDamage(damage, source, target, move):
    # function (damage, source, target, move) {
	# 			if (target !== source && target.side === this.effectData.target) {
	# 				if ((target.side.sideConditions['reflect'] && this.getCategory(move) === 'Physical') ||
	# 						(target.side.sideConditions['lightscreen'] && this.getCategory(move) === 'Special')) {
	# 					return;
	# 				}
	# 				if (!move.crit && !move.infiltrates) {
	# 					this.debug('Aurora Veil weaken');
	# 					if (target.side.active.length > 1) return this.chainModify([0xAAC, 0x1000]);
	# 					return this.chainModify(0.5);
	# 				}
	# 			}
	# 		}
    pass

def onStart(side):
    # function (side) {
	# 			this.add('-sidestart', side, '"move": Aurora Veil');
	# 		}
    pass

def onEnd(side):
    #  function (side) {
	# 			this.add('-sideend', side, '"move": Aurora Veil');
	# 		}
    pass