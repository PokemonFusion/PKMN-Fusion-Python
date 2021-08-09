def durationCallback(**bvalues):
	"""function (target, source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onBeforeMove(**bvalues):
	"""function (pokemon, target, move) {
				if (move.flags['heal'] && !move.isZ && !move.isMax) {
					this.add('cant', pokemon, 'move: Heal Block', move);
					return false;
				}
			}
	""" 
	pass

def onDisableMove(**bvalues):
	"""function (pokemon) {
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					if (this.dex.moves.get(moveSlot.id).flags['heal']) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Heal Block');
			}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, pokemon, target) {
				if (move.flags['heal'] && !move.isZ && !move.isMax) {
					this.add('cant', pokemon, 'move: Heal Block', move);
					return false;
				}
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (target, source) {
				this.add('-fail', target, 'move: Heal Block'); // Succeeds to supress downstream messages
				if (!source.moveThisTurnResult) {
					source.moveThisTurnResult = false;
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon, source) {
				this.add('-start', pokemon, 'move: Heal Block');
				source.moveThisTurnResult = true;
			}
	""" 
	pass

def onTryHeal(**bvalues):
	"""function (damage, target, source, effect) {
				if (((effect === null || effect === void 0 ? void 0 : effect.id) === 'zpower') || this.effectState.isZ)
					return damage;
				return false;
			}
	""" 
	pass
