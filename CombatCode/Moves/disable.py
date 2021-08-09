def onBeforeMove(**bvalues):
	"""function (attacker, defender, move) {
				if (!move.isZ && move.id === this.effectState.move) {
					this.add('cant', attacker, 'Disable', move);
					return false;
				}
			}
	""" 
	pass

def onDisableMove(**bvalues):
	"""function (pokemon) {
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					if (moveSlot.id === this.effectState.move) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Disable');
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon, source, effect) {
				// The target hasn't taken its turn, or Cursed Body activated and the move was not used through Dancer or Instruct
				if (this.queue.willMove(pokemon) ||
					(pokemon === this.activePokemon && this.activeMove && !this.activeMove.isExternal)) {
					this.effectState.duration--;
				}
				if (!pokemon.lastMove) {
					this.debug("Pokemon hasn't moved yet");
					return false;
				}
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					if (moveSlot.id === pokemon.lastMove.id) {
						if (!moveSlot.pp) {
							this.debug('Move out of PP');
							return false;
						}
					}
				}
				if (effect.effectType === 'Ability') {
					this.add('-start', pokemon, 'Disable', pokemon.lastMove.name, '[from] ability: Cursed Body', '[of] ' + source);
				}
				else {
					this.add('-start', pokemon, 'Disable', pokemon.lastMove.name);
				}
				this.effectState.move = pokemon.lastMove.id;
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (!target.lastMove || target.lastMove.isZ || target.lastMove.isMax || target.lastMove.id === 'struggle') {
				return false;
			}
		}
	""" 
	pass
