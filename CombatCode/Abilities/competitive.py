def onAfterEachBoost(**bvalues):
	"""function (boost, target, source, effect) {
			if (!source || target.isAlly(source)) {
				if (effect.id === 'stickyweb') {
					this.hint("Court Change Sticky Web counts as lowering your own Speed, and Competitive only affects stats lowered by foes.", True, source.side);
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
				this.add('-ability', target, 'Competitive');
				this.boost({ spa: 2 }, target, target, null, True);
			}
		}
	""" 
	pass
