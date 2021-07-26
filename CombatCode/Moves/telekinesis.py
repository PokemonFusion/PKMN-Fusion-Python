def onStart(**bvalues):
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

def onAccuracy(**bvalues):
	"""function (accuracy, target, source, move) {
				if (move && !move.ohko) return true;
			}
	""" 
	pass

def onImmunity(**bvalues):
	"""function (type) {
				if (type === 'Ground') return false;
			}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
				if (pokemon.baseTemplate.species === 'Gengar-Mega') {
					delete pokemon.volatiles['telekinesis'];
					this.add('-end', pokemon, 'Telekinesis', '[silent]');
				}
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'Telekinesis');
			}
	""" 
	pass
