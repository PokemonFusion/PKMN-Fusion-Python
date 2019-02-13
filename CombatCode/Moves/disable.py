def onTryHit(datadic : dict):
	"""function (target) {
			if (!target.lastMove || target.lastMove.isZ) {
				return false;
			}
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon, source, effect) {
				if (!this.willMove(pokemon)) {
					this.effectData.duration++;
				}
				if (!pokemon.lastMove) {
					this.debug('pokemon hasn't moved yet');
					return false;
				}
				for (const moveSlot of pokemon.moveSlots) {
					if (moveSlot.id === pokemon.lastMove.id) {
						if (!moveSlot.pp) {
							this.debug('Move out of PP');
							return false;
						} else {
							if (effect.id === 'cursedbody') {
								this.add('-start', pokemon, 'Disable', moveSlot.move, '[from] ability: Cursed Body', '[of] ' + source);
							} else {
								this.add('-start', pokemon, 'Disable', moveSlot.move);
							}
							this.effectData.move = pokemon.lastMove.id;
							return;
						}
					}
				}
				// this can happen if Disable works on a Z-move
				return false;
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (pokemon) {
				this.add('-end', pokemon, 'Disable');
			}
	""" 
	pass

def onBeforeMove(datadic : dict):
	"""function (attacker, defender, move) {
				if (move.id === this.effectData.move) {
					this.add('cant', attacker, 'Disable', move);
					return false;
				}
			}
	""" 
	pass

def onDisableMove(datadic : dict):
	"""function (pokemon) {
				for (const moveSlot of pokemon.moveSlots) {
					if (moveSlot.id === this.effectData.move) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass
