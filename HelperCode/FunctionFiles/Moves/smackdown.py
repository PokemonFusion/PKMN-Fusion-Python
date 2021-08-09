def onRestart (pokemon):
	"""function (pokemon) {
				if (pokemon.removeVolatile('fly') || pokemon.removeVolatile('bounce')) {
					this.queue.cancelMove(pokemon);
					this.add('-start', pokemon, 'Smack Down');
				}
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				var applies = false;
				if (pokemon.hasType('Flying') || pokemon.hasAbility('levitate'))
					applies = true;
				if (pokemon.hasItem('ironball') || pokemon.volatiles['ingrain'] ||
					this.field.getPseudoWeather('gravity'))
					applies = false;
				if (pokemon.removeVolatile('fly') || pokemon.removeVolatile('bounce')) {
					applies = true;
					this.queue.cancelMove(pokemon);
					pokemon.removeVolatile('twoturnmove');
				}
				if (pokemon.volatiles['magnetrise']) {
					applies = true;
					delete pokemon.volatiles['magnetrise'];
				}
				if (pokemon.volatiles['telekinesis']) {
					applies = true;
					delete pokemon.volatiles['telekinesis'];
				}
				if (!applies)
					return false;
				this.add('-start', pokemon, 'Smack Down');
			}
	""" 
	pass