def basePowerCallback (pokemon, target):
	"""function (pokemon, target) {
			var targetWeight = target.getWeight();
			if (targetWeight >= 2000) {
				return 120;
			}
			if (targetWeight >= 1000) {
				return 100;
			}
			if (targetWeight >= 500) {
				return 80;
			}
			if (targetWeight >= 250) {
				return 60;
			}
			if (targetWeight >= 100) {
				return 40;
			}
			return 20;
		}
	""" 
	pass

def onTryHit (target, pokemon, move):
	"""function (target, pokemon, move) {
			if (target.volatiles['dynamax']) {
				this.add('-fail', pokemon, 'Dynamax');
				this.attrLastMove('[still]');
				return null;
			}
		}
	""" 
	pass