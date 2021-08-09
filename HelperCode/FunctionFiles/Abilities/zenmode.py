def onResidual (pokemon):
	"""function (pokemon) {
			if (pokemon.baseSpecies.baseSpecies !== 'Darmanitan' || pokemon.transformed) {
				return;
			}
			if (pokemon.hp <= pokemon.maxhp / 2 && !['Zen', 'Galar-Zen'].includes(pokemon.species.forme)) {
				pokemon.addVolatile('zenmode');
			}
			else if (pokemon.hp > pokemon.maxhp / 2 && ['Zen', 'Galar-Zen'].includes(pokemon.species.forme)) {
				pokemon.addVolatile('zenmode'); // in case of base Darmanitan-Zen
				pokemon.removeVolatile('zenmode');
			}
		}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
			if (!pokemon.volatiles['zenmode'] || !pokemon.hp)
				return;
			pokemon.transformed = False;
			delete pokemon.volatiles['zenmode'];
			if (pokemon.species.baseSpecies === 'Darmanitan' && pokemon.species.battleOnly) {
				pokemon.formeChange(pokemon.species.battleOnly, this.effect, False, '[silent]');
			}
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				if (!pokemon.species.name.includes('Galar')) {
					if (pokemon.species.id !== 'darmanitanzen')
						pokemon.formeChange('Darmanitan-Zen');
				}
				else {
					if (pokemon.species.id !== 'darmanitangalarzen')
						pokemon.formeChange('Darmanitan-Galar-Zen');
				}
			}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
				if (['Zen', 'Galar-Zen'].includes(pokemon.species.forme)) {
					pokemon.formeChange(pokemon.species.battleOnly);
				}
			}
	""" 
	pass