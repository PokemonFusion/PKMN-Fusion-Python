def onStart(**bvalues):
	"""function (pokemon) {
			pokemon.addVolatile('metronome');
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.effectData.numConsecutive = 0;
				this.effectData.lastMove = '';
			}
	""" 
	pass

def onTryMove(**bvalues):
	"""function (pokemon, target, move) {
				if (!pokemon.hasItem('metronome')) {
					pokemon.removeVolatile('metronome');
					return;
				}
				if (this.effectData.lastMove === move.id) {
					this.effectData.numConsecutive++;
				} else {
					this.effectData.numConsecutive = 0;
				}
				this.effectData.lastMove = move.id;
			}
	""" 
	pass

def onModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
				let numConsecutive = this.effectData.numConsecutive > 5 ? 5 : this.effectData.numConsecutive;
				let dmgMod = [0x1000, 0x1333, 0x1666, 0x1999, 0x1CCC, 0x2000];
				return this.chainModify([dmgMod[numConsecutive], 0x1000]);
			}
	""" 
	pass
