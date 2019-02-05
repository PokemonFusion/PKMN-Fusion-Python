def onBoost(datadic : dict):
	"""function (boost, target, source, effect) {
			if (source && target === source) return;
			if (boost.accuracy && boost.accuracy < 0) {
				delete boost.accuracy;
				if (!effect.secondaries) this.add("-fail", target, "unboost", "accuracy", "[from] ability: Keen Eye", "[of] " + target);
			}
		}
	""" 
	pass

def onModifyMove(datadic : dict):
	"""function (move) {
			move.ignoreEvasion = true;
		}
	""" 
	pass
