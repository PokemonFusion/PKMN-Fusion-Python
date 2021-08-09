def onStart(**bvalues):
	"""function (pokemon) {
			if (this.field.terrain) {
				pokemon.addVolatile('mimicry');
			}
			else {
				var types = pokemon.baseSpecies.types;
				if (pokemon.getTypes().join() === types.join() || !pokemon.setType(types))
					return;
				this.add('-start', pokemon, 'typechange', types.join('/'), '[from] ability: Mimicry');
				this.hint("Transform Mimicry changes you to your original un-transformed types.");
			}
		}
	""" 
	pass

def onAnyTerrainStart(**bvalues):
	"""function () {
			var pokemon = this.effectState.target;
			delete pokemon.volatiles['mimicry'];
			pokemon.addVolatile('mimicry');
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			delete pokemon.volatiles['mimicry'];
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				var newType;
				switch (this.field.terrain) {
					case 'electricterrain':
						newType = 'Electric';
						break;
					case 'grassyterrain':
						newType = 'Grass';
						break;
					case 'mistyterrain':
						newType = 'Fairy';
						break;
					case 'psychicterrain':
						newType = 'Psychic';
						break;
				}
				if (!newType || pokemon.getTypes().join() === newType || !pokemon.setType(newType))
					return;
				this.add('-start', pokemon, 'typechange', newType, '[from] ability: Mimicry');
			}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
				if (!this.field.terrain) {
					var types = pokemon.species.types;
					if (pokemon.getTypes().join() === types.join() || !pokemon.setType(types))
						return;
					this.add('-activate', pokemon, 'ability: Mimicry');
					this.add('-end', pokemon, 'typechange', '[silent]');
					pokemon.removeVolatile('mimicry');
				}
			}
	""" 
	pass
