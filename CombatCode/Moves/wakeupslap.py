def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			if (target.status === 'slp' || target.hasAbility('comatose'))
				return move.basePower * 2;
			return move.basePower;
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target) {
			if (target.status === 'slp')
				target.cureStatus();
		}
	""" 
	pass
