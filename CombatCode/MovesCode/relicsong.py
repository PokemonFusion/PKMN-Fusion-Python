def onHit (target, pokemon, move):
	"""function (target, pokemon, move) {
			if (pokemon.baseTemplate.baseSpecies === 'Meloetta' && !pokemon.transformed) {
				move.willChangeForme = true;
			}
		}
	""" 
	pass

def onAfterMoveSecondarySelf (pokemon, target, move):
	"""function (pokemon, target, move) {
			if (move.willChangeForme) {
				pokemon.formeChange(pokemon.template.speciesid === 'meloettapirouette' ? 'Meloetta' : 'Meloetta-Pirouette', this.effect, false, '[msg]');
			}
		}
	""" 
	pass