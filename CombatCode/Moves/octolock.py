def onResidual(**bvalues):
	"""function (pokemon) {
				var source = this.effectState.source;
				if (source && (!source.isActive || source.hp <= 0 || !source.activeTurns)) {
					delete pokemon.volatiles['octolock'];
					this.add('-end', pokemon, 'Octolock', '[partiallytrapped]', '[silent]');
					return;
				}
				this.boost({ def: -1, spd: -1 }, pokemon, source, this.dex.getActiveMove('octolock'));
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon, source) {
				this.add('-start', pokemon, 'move: Octolock', '[of] ' + source);
			}
	""" 
	pass

def onTrapPokemon(**bvalues):
	"""function (pokemon) {
				if (this.effectState.source && this.effectState.source.isActive)
					pokemon.tryTrap();
			}
	""" 
	pass

def onTryImmunity(**bvalues):
	"""function (target) {
			return this.dex.getImmunity('trapped', target);
		}
	""" 
	pass
