def onHit(**bvalues):
	"""function (target, pokemon, move) {
			if (pokemon.baseTemplate.baseSpecies === 'Meloetta' && !pokemon.transformed) {
				move.willChangeForme = true;
			}
		}
	""" 
	pass

def onAfterMoveSecondarySelf(**bvalues):
	"""function (pokemon, target, move) {
			if (move.willChangeForme) {
				pokemon.formeChange(pokemon.template.speciesid === 'meloettapirouette' ? 'Meloetta' : 'Meloetta-Pirouette', this.effect, false, '[msg]');
			}
		}
	""" 
	pass
