def onBasePower(**bvalues):
	"""function (basePower, source) {
			if (this.field.isTerrain('psychicterrain') && source.isGrounded()) {
				this.debug('terrain buff');
				return this.chainModify(1.5);
			}
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, source, target) {
			if (this.field.isTerrain('psychicterrain') && source.isGrounded()) {
				move.target = 'allAdjacentFoes';
			}
		}
	""" 
	pass
