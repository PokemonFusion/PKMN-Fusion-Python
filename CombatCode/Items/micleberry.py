def onSourceAccuracy(**bvalues):
	"""function (accuracy, target, source, move) {
				if (!move.ohko) {
					this.add('-enditem', source, 'Micle Berry');
					source.removeVolatile('micleberry');
					if (typeof accuracy === 'number') {
						return this.chainModify([4915, 4096]);
					}
				}
			}
	""" 
	pass

def onEat(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('micleberry');
		}
	""" 
	pass

def onResidual(**bvalues):
	"""function (pokemon) {
			if (pokemon.hp <= pokemon.maxhp / 4 || (pokemon.hp <= pokemon.maxhp / 2 && pokemon.hasAbility('gluttony'))) {
				pokemon.eatItem();
			}
		}
	""" 
	pass
