def onBeforeSwitchIn(**bvalues):
	"""function (pokemon) {
			pokemon.illusion = null;
			// yes, you can Illusion an active pokemon but only if it's to your right
			for (var i = pokemon.side.pokemon.length - 1; i > pokemon.position; i--) {
				var possibleTarget = pokemon.side.pokemon[i];
				if (!possibleTarget.fainted) {
					pokemon.illusion = possibleTarget;
					break;
				}
			}
		}
	""" 
	pass

def onDamagingHit(**bvalues):
	"""function (damage, target, source, move) {
			if (target.illusion) {
				this.singleEvent('End', this.dex.abilities.get('Illusion'), target.abilityState, target, source, move);
			}
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			if (pokemon.illusion) {
				this.debug('illusion cleared');
				pokemon.illusion = null;
				var details = pokemon.species.name + (pokemon.level === 100 ? '' : ', L' + pokemon.level) +
					(pokemon.gender === '' ? '' : ', ' + pokemon.gender) + (pokemon.set.shiny ? ', shiny' : '');
				this.add('replace', pokemon, details);
				this.add('-end', pokemon, 'Illusion');
			}
		}
	""" 
	pass

def onFaint(**bvalues):
	"""function (pokemon) {
			pokemon.illusion = null;
		}
	""" 
	pass
