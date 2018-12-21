def onEffectiveness (typeMod, type, move):
	"""function (typeMod, type, move) {
			if (move.type !== 'Ground') return;
			let target = this.activeTarget;
			if (!target) return; // avoid crashing when called from a chat plugin
			// ignore effectiveness if the target is Flying type and immune to Ground
			if (!target.runImmunity('Ground')) {
				if (target.hasType('Flying')) return 0;
			}
		}
	""" 
	pass