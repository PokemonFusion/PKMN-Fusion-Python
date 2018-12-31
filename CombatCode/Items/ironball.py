def onEffectiveness (typeMod, target, type, move):
	"""function (typeMod, target, type, move) {
			if (!target) return;
			if (target.volatiles['ingrain'] || target.volatiles['smackdown'] || this.getPseudoWeather('gravity')) return;
			if (move.type === 'Ground' && target.hasType('Flying')) return 0;
		}
	""" 
	pass

def onModifySpe (spe):
	"""function (spe) {
			return this.chainModify(0.5);
		}
	""" 
	pass