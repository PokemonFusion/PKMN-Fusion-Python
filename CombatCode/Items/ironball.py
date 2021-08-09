def onEffectiveness(**bvalues):
	"""function (typeMod, target, type, move) {
			if (!target)
				return;
			if (target.volatiles['ingrain'] || target.volatiles['smackdown'] || this.field.getPseudoWeather('gravity'))
				return;
			if (move.type === 'Ground' && target.hasType('Flying'))
				return 0;
		}
	""" 
	pass

def onModifySpe(**bvalues):
	"""function (spe) {
			return this.chainModify(0.5);
		}
	""" 
	pass
