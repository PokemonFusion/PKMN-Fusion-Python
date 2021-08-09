def onAccuracy(**bvalues):
	"""function (accuracy, target, source, move) {
				if (move && !move.ohko)
					return true;
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (target) {
				this.add('-end', target, 'Telekinesis');
			}
	""" 
	pass

def onImmunity(**bvalues):
	"""function (type) {
				if (type === 'Ground')
					return false;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				if (['Diglett', 'Dugtrio', 'Palossand', 'Sandygast'].includes(target.baseSpecies.baseSpecies) ||
					target.baseSpecies.name === 'Gengar-Mega') {
					this.add('-immune', target);
					return null;
				}
				if (target.volatiles['smackdown'] || target.volatiles['ingrain'])
					return false;
				this.add('-start', target, 'Telekinesis');
			}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
				if (pokemon.baseSpecies.name === 'Gengar-Mega') {
					delete pokemon.volatiles['telekinesis'];
					this.add('-end', pokemon, 'Telekinesis', '[silent]');
				}
			}
	""" 
	pass

def onTry(**bvalues):
	"""function (source, target, move) {
			// Additional Gravity check for Z-move variant
			if (this.field.getPseudoWeather('Gravity')) {
				this.attrLastMove('[still]');
				this.add('cant', source, 'move: Gravity', move);
				return null;
			}
		}
	""" 
	pass
