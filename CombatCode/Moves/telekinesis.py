def onStart (target):
	"""function (target) {
				if (['Diglett', 'Dugtrio', 'Palossand', 'Sandygast'].includes(target.baseTemplate.baseSpecies) ||
						target.baseTemplate.species === 'Gengar-Mega') {
					this.add('-immune', target);
					return null;
				}
				if (target.volatiles['smackdown'] || target.volatiles['ingrain']) return false;
				this.add('-start', target, 'Telekinesis');
			}
	""" 
	pass

def onAccuracy (accuracy, target, source, move):
	"""function (accuracy, target, source, move) {
				if (move && !move.ohko) return true;
			}
	""" 
	pass

def onImmunity (type):
	"""function (type) {
				if (type === 'Ground') return false;
			}
	""" 
	pass

def onUpdate (pokemon):
	"""function (pokemon) {
				if (pokemon.baseTemplate.species === 'Gengar-Mega') {
					delete pokemon.volatiles['telekinesis'];
					this.add('-end', pokemon, 'Telekinesis', '[silent]');
				}
			}
	""" 
	pass

def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'Telekinesis');
			}
	""" 
	pass