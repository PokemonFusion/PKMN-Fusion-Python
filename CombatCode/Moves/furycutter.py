def basePowerCallback (pokemon, target, move):
	"""function (pokemon, target, move) {
			if (!pokemon.volatiles.furycutter) {
				pokemon.addVolatile('furycutter');
			}
			return this.clampIntRange(move.basePower * pokemon.volatiles.furycutter.multiplier, 1, 160);
		}
	""" 
	pass

def onHit (target, source):
	"""function (target, source) {
			source.addVolatile('furycutter');
		}
	""" 
	pass

def onStart ():
	"""function () {
				this.effectData.multiplier = 1;
			}
	""" 
	pass

def onRestart ():
	"""function () {
				if (this.effectData.multiplier < 4) {
					this.effectData.multiplier <<= 1;
				}
				this.effectData.duration = 2;
			}
	""" 
	pass