def onStart(**bvalues):
	"""function (pokemon) {
			pokemon.abilityState.choiceLock = "";
		}
	""" 
	pass

def onBeforeMove(**bvalues):
	"""function (pokemon, target, move) {
			if (move.isZOrMaxPowered || move.id === 'struggle')
				return;
			if (pokemon.abilityState.choiceLock && pokemon.abilityState.choiceLock !== move.id) {
				// Fails unless ability is being ignored (these events will not run), no PP lost.
				this.addMove('move', pokemon, move.name);
				this.attrLastMove('[still]');
				this.debug("Disabled by Gorilla Tactics");
				this.add('-fail', pokemon);
				return False;
			}
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, pokemon) {
			if (pokemon.abilityState.choiceLock || move.isZOrMaxPowered || move.id === 'struggle')
				return;
			pokemon.abilityState.choiceLock = move.id;
		}
	""" 
	pass

def onModifyAtk(**bvalues):
	"""function (atk, pokemon) {
			if (pokemon.volatiles['dynamax'])
				return;
			// PLACEHOLDER
			this.debug('Gorilla Tactics Atk Boost');
			return this.chainModify(1.5);
		}
	""" 
	pass

def onDisableMove(**bvalues):
	"""function (pokemon) {
			if (!pokemon.abilityState.choiceLock)
				return;
			if (pokemon.volatiles['dynamax'])
				return;
			for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
				var moveSlot = _a[_i];
				if (moveSlot.id !== pokemon.abilityState.choiceLock) {
					pokemon.disableMove(moveSlot.id, False, this.effectState.sourceEffect);
				}
			}
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
			pokemon.abilityState.choiceLock = "";
		}
	""" 
	pass
