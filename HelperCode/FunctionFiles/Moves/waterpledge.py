def basePowerCallback (target, source, move):
	"""function (target, source, move) {
			if (['firepledge', 'grasspledge'].includes(move.sourceEffect)) {
				this.add('-combine');
				return 150;
			}
			return 80;
		}
	""" 
	pass

def onModifyMove (move, pokemon):
	"""function (move, pokemon) {
				var _a;
				if (move.secondaries && move.id !== 'secretpower') {
					this.debug('doubling secondary chance');
					for (var _i = 0, _b = move.secondaries; _i < _b.length; _i++) {
						var secondary = _b[_i];
						if (pokemon.hasAbility('serenegrace') && secondary.volatileStatus === 'flinch')
							continue;
						if (secondary.chance)
							secondary.chance *= 2;
					}
					if ((_a = move.self) === null || _a === void 0 ? void 0 : _a.chance)
						move.self.chance *= 2;
				}
			}
	""" 
	pass

def onSideEnd (targetSide):
	"""function (targetSide) {
				this.add('-sideend', targetSide, 'Water Pledge');
			}
	""" 
	pass

def onSideStart (targetSide):
	"""function (targetSide) {
				this.add('-sidestart', targetSide, 'Water Pledge');
			}
	""" 
	pass

def onModifyMove (move):
	"""function (move) {
			if (move.sourceEffect === 'grasspledge') {
				move.type = 'Grass';
				move.forceSTAB = true;
				move.sideCondition = 'grasspledge';
			}
			if (move.sourceEffect === 'firepledge') {
				move.type = 'Water';
				move.forceSTAB = true;
				move.self = { sideCondition: 'waterpledge' };
			}
		}
	""" 
	pass

def onPrepareHit (target, source, move):
	"""function (target, source, move) {
			for (var _i = 0, _a = this.queue; _i < _a.length; _i++) {
				var action = _a[_i];
				if (action.choice !== 'move')
					continue;
				var otherMove = action.move;
				var otherMoveUser = action.pokemon;
				if (!otherMove || !action.pokemon || !otherMoveUser.isActive ||
					otherMoveUser.fainted || action.maxMove || action.zmove) {
					continue;
				}
				if (otherMoveUser.isAlly(source) && ['firepledge', 'grasspledge'].includes(otherMove.id)) {
					this.queue.prioritizeAction(action, move);
					this.add('-waiting', source, otherMoveUser);
					return null;
				}
			}
		}
	""" 
	pass