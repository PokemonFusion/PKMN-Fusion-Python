def onAfterEachBoost (boost, target, source, effect):
	"""function (boost, target, source, effect) {
			if (!source || target.isAlly(source)) {
				if (effect.id === 'stickyweb') {
					this.hint("Court Change Sticky Web counts as lowering your own Speed, and Defiant only affects stats lowered by foes.", True, source.side);
				}
				return;
			}
			var statsLowered = False;
			var i;
			for (i in boost) {
				if (boost[i] < 0) {
					statsLowered = True;
				}
			}
			if (statsLowered) {
				this.add('-ability', target, 'Defiant');
				this.boost({ atk: 2 }, target, target, null, True);
			}
		}
	""" 
	pass