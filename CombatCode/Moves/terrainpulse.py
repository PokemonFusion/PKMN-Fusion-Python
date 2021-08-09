def onModifyMove(**bvalues):
	"""function (move, pokemon) {
			if (this.field.terrain && pokemon.isGrounded()) {
				move.basePower *= 2;
			}
		}
	""" 
	pass

def onModifyType(**bvalues):
	"""function (move, pokemon) {
			if (!pokemon.isGrounded())
				return;
			switch (this.field.terrain) {
				case 'electricterrain':
					move.type = 'Electric';
					break;
				case 'grassyterrain':
					move.type = 'Grass';
					break;
				case 'mistyterrain':
					move.type = 'Fairy';
					break;
				case 'psychicterrain':
					move.type = 'Psychic';
					break;
			}
		}
	""" 
	pass
