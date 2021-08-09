def durationCallback (source, effect):
	"""function (source, effect) {
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
				if (move.flags['gravity'] && !move.isZ) {
					this.add('cant', pokemon, 'move: Gravity', move);
					return false;
				}
			}
	""" 
	pass

def onDisableMove (pokemon):
	"""function (pokemon) {
				for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
					var moveSlot = _a[_i];
					if (this.dex.moves.get(moveSlot.id).flags['gravity']) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onFieldEnd ():
	"""function () {
				this.add('-fieldend', 'move: Gravity');
			}
	""" 
	pass

def onFieldStart ():
	"""function () {
				this.add('-fieldstart', 'move: Gravity');
				for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
					var pokemon = _a[_i];
					var applies = false;
					if (pokemon.removeVolatile('bounce') || pokemon.removeVolatile('fly')) {
						applies = true;
						this.queue.cancelMove(pokemon);
						pokemon.removeVolatile('twoturnmove');
					}
					if (pokemon.volatiles['skydrop']) {
						applies = true;
						this.queue.cancelMove(pokemon);
						if (pokemon.volatiles['skydrop'].source) {
							this.add('-end', pokemon.volatiles['twoturnmove'].source, 'Sky Drop', '[interrupt]');
						}
						pokemon.removeVolatile('skydrop');
						pokemon.removeVolatile('twoturnmove');
					}
					if (pokemon.volatiles['magnetrise']) {
						applies = true;
						delete pokemon.volatiles['magnetrise'];
					}
					if (pokemon.volatiles['telekinesis']) {
						applies = true;
						delete pokemon.volatiles['telekinesis'];
					}
					if (applies)
						this.add('-activate', pokemon, 'move: Gravity');
				}
			}
	""" 
	pass

def onModifyAccuracy (accuracy):
	"""function (accuracy) {
				if (typeof accuracy !== 'number')
					return;
				return this.chainModify([6840, 4096]);
			}
	""" 
	pass

def onModifyMove (move, pokemon, target):
	"""function (move, pokemon, target) {
				if (move.flags['gravity'] && !move.isZ) {
					this.add('cant', pokemon, 'move: Gravity', move);
					return false;
				}
			}
	""" 
	pass