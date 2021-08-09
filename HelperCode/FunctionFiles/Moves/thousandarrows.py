def onEffectiveness (typeMod, target, type, move):
	"""function (typeMod, target, type, move) {
			if (move.type !== 'Ground')
				return;
			if (!target)
				return; // avoid crashing when called from a chat plugin
			// ignore effectiveness if the target is Flying type and immune to Ground
			if (!target.runImmunity('Ground')) {
				if (target.hasType('Flying'))
					return 0;
			}
		}
	""" 
	pass