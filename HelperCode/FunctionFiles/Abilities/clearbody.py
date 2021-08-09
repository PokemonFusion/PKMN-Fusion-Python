def onBoost (boost, target, source, effect):
	"""function (boost, target, source, effect) {
			if (source && target === source)
				return;
			var showMsg = False;
			var i;
			for (i in boost) {
				if (boost[i] < 0) {
					delete boost[i];
					showMsg = True;
				}
			}
			if (showMsg && !effect.secondaries && effect.id !== 'octolock') {
				this.add("-fail", target, "unboost", "[from] ability: Clear Body", "[of] " + target);
			}
		}
	""" 
	pass