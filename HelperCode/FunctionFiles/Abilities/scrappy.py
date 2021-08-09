def onModifyMove (move):
	"""function (move) {
			if (!move.ignoreImmunity)
				move.ignoreImmunity = {};
			if (move.ignoreImmunity !== True) {
				move.ignoreImmunity['Fighting'] = True;
				move.ignoreImmunity['Normal'] = True;
			}
		}
	""" 
	pass

def onBoost (boost, target, source, effect):
	"""function (boost, target, source, effect) {
			if (effect.id === 'intimidate') {
				delete boost.atk;
				this.add('-fail', target, 'unboost', 'Attack', '[from] ability: Scrappy', '[of] ' + target);
			}
		}
	""" 
	pass