def onAfterBoost(**bvalues):
	"""function (boost, target, source, effect) {
			var _a;
			if (((_a = this.activeMove) === null || _a === void 0 ? void 0 : _a.id) === 'partingshot')
				return;
			var eject = false;
			var i;
			for (i in boost) {
				if (boost[i] < 0) {
					eject = true;
				}
			}
			if (eject) {
				if (target.hp) {
					if (!this.canSwitch(target.side))
						return;
					for (var _i = 0, _b = this.getAllActive(); _i < _b.length; _i++) {
						var pokemon = _b[_i];
						if (pokemon.switchFlag === true)
							return;
					}
					if (target.useItem())
						target.switchFlag = true;
				}
			}
		}
	""" 
	pass
