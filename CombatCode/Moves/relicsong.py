def onAfterMoveSecondarySelf(**bvalues):
	"""function (pokemon, target, move) {
			if (move.willChangeForme) {
				var meloettaForme = pokemon.species.id === 'meloettapirouette' ? '' : '-Pirouette';
				pokemon.formeChange('Meloetta' + meloettaForme, this.effect, false, '[msg]');
			}
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, pokemon, move) {
			if (pokemon.baseSpecies.baseSpecies === 'Meloetta' && !pokemon.transformed) {
				move.willChangeForme = true;
			}
		}
	""" 
	pass
