def durationCallback (target, source, effect):
	"""function (target, source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onBeforeMove (pokemon, target, move):
	"""function (pokemon, target, move) {
				if (move.flags['heal'] && !move.isZ && !move.isMax) {
					this.add('cant', pokemon, 'move: Heal Block', move);
					return false;
				}
			}
	""" 
	pass

def onDisableMove (pokemon):
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

def onEnd (pokemon):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Heal Block');
			}
	""" 
	pass

def onModifyMove (move, pokemon, target):
	"""function (move, pokemon, target) {
				if (move.flags['heal'] && !move.isZ && !move.isMax) {
					this.add('cant', pokemon, 'move: Heal Block', move);
					return false;
				}
			}
	""" 
	pass

def onRestart (target, source):
	"""function (target, source) {
				this.add('-fail', target, 'move: Heal Block'); // Succeeds to supress downstream messages
				if (!source.moveThisTurnResult) {
					source.moveThisTurnResult = false;
				}
			}
	""" 
	pass

def onStart (pokemon, source):
	"""function (pokemon, source) {
				this.add('-start', pokemon, 'move: Heal Block');
				source.moveThisTurnResult = true;
			}
	""" 
	pass

def onTryHeal (damage, target, source, effect):
	"""function (damage, target, source, effect) {
				if (((effect === null || effect === void 0 ? void 0 : effect.id) === 'zpower') || this.effectState.isZ)
					return damage;
				return false;
			}
	""" 
	pass