def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			if (!pokemon.volatiles.furycutter) {
				pokemon.addVolatile('furycutter');
			}
			return this.clampIntRange(move.basePower * pokemon.volatiles.furycutter.multiplier, 1, 160);
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source) {
			source.addVolatile('furycutter');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function () {
				this.effectData.multiplier = 1;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function () {
				if (this.effectData.multiplier < 4) {
					this.effectData.multiplier <<= 1;
				}
				this.effectData.duration = 2;
			}
	""" 
	pass
