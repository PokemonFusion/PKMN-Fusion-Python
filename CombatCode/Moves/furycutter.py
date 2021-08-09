def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			if (!pokemon.volatiles['furycutter'] || move.hit === 1) {
				pokemon.addVolatile('furycutter');
			}
			return this.clampIntRange(move.basePower * pokemon.volatiles['furycutter'].multiplier, 1, 160);
		}
	""" 
	pass

def onRestart(**bvalues):
	"""function () {
				if (this.effectState.multiplier < 4) {
					this.effectState.multiplier <<= 1;
				}
				this.effectState.duration = 2;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function () {
				this.effectState.multiplier = 1;
			}
	""" 
	pass
