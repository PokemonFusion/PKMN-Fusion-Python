def onModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
				var dmgMod = [4096, 4915, 5734, 6553, 7372, 8192];
				var numConsecutive = this.effectState.numConsecutive > 5 ? 5 : this.effectState.numConsecutive;
				this.debug("Current Metronome boost: " + dmgMod[numConsecutive] + "/4096");
				return this.chainModify([dmgMod[numConsecutive], 4096]);
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.effectState.lastMove = '';
				this.effectState.numConsecutive = 0;
			}
	""" 
	pass

def onTryMove(**bvalues):
	"""function (pokemon, target, move) {
				if (!pokemon.hasItem('metronome')) {
					pokemon.removeVolatile('metronome');
					return;
				}
				if (this.effectState.lastMove === move.id && pokemon.moveLastTurnResult) {
					this.effectState.numConsecutive++;
				}
				else if (pokemon.volatiles['twoturnmove'] && this.effectState.lastMove !== move.id) {
					this.effectState.numConsecutive = 1;
				}
				else {
					this.effectState.numConsecutive = 0;
				}
				this.effectState.lastMove = move.id;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('metronome');
		}
	""" 
	pass
