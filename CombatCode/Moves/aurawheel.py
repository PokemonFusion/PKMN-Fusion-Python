def onModifyType(**bvalues):
	"""function (move, pokemon) {
			if (pokemon.species.name === 'Morpeko-Hangry') {
				move.type = 'Dark';
			}
			else {
				move.type = 'Electric';
			}
		}
	""" 
	pass

def onTry(**bvalues):
	"""function (source) {
			if (source.species.baseSpecies === 'Morpeko') {
				return;
			}
			this.attrLastMove('[still]');
			this.add('-fail', source, 'move: Aura Wheel');
			this.hint("Only a Pokemon whose form is Morpeko or Morpeko-Hangry can use this move.");
			return null;
		}
	""" 
	pass
