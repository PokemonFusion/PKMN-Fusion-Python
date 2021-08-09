def onHit (target):
	"""function (target) {
			var newType = 'Normal';
			if (this.field.isTerrain('electricterrain')) {
				newType = 'Electric';
			}
			else if (this.field.isTerrain('grassyterrain')) {
				newType = 'Grass';
			}
			else if (this.field.isTerrain('mistyterrain')) {
				newType = 'Fairy';
			}
			else if (this.field.isTerrain('psychicterrain')) {
				newType = 'Psychic';
			}
			if (target.getTypes().join() === newType || !target.setType(newType))
				return false;
			this.add('-start', target, 'typechange', newType);
		}
	""" 
	pass