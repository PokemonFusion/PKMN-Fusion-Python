def onResidual(datadic : dict):
	"""function (pokemon) {
			if (pokemon.baseTemplate.baseSpecies !== 'Darmanitan' || pokemon.transformed) {
				return;
			}
			if (pokemon.hp <= pokemon.maxhp / 2 && pokemon.template.speciesid === 'darmanitan') {
				pokemon.addVolatile('zenmode');
			} else if (pokemon.hp > pokemon.maxhp / 2 && pokemon.template.speciesid === 'darmanitanzen') {
				pokemon.addVolatile('zenmode'); // in case of base Darmanitan-Zen
				pokemon.removeVolatile('zenmode');
			}
		}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
			if (!pokemon.volatiles['zenmode'] || !pokemon.hp) return;
			pokemon.transformed = false;
			delete pokemon.volatiles['zenmode'];
			pokemon.formeChange('Darmanitan', this.effect, false, '[silent]');
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				if (pokemon.template.speciesid !== 'darmanitanzen') pokemon.formeChange('Darmanitan-Zen');
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
				pokemon.formeChange('Darmanitan');
			}
	""" 
	pass
