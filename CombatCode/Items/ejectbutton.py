def onAfterMoveSecondary(**bvalues):
	"""function (target, source, move) {
			if (source && source !== target && target.hp && move && move.category !== 'Status' && !move.isFutureMove) {
				if (!this.canSwitch(target.side) || target.forceSwitchFlag || target.beingCalledBack)
					return;
				for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
					var pokemon = _a[_i];
					if (pokemon.switchFlag === true)
						return;
				}
				target.switchFlag = true;
				if (target.useItem()) {
					source.switchFlag = false;
				}
				else {
					target.switchFlag = false;
				}
			}
		}
	""" 
	pass
