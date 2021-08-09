def basePowerCallback(**bvalues):
	"""function (target, source, move) {
			if (['grasspledge', 'waterpledge'].includes(move.sourceEffect)) {
				this.add('-combine');
				return 150;
			}
			return 80;
		}
	""" 
	pass

def onResidual(**bvalues):
	"""function (pokemon) {
				if (!pokemon.hasType('Fire'))
					this.damage(pokemon.baseMaxhp / 8, pokemon);
			}
	""" 
	pass

def onSideEnd(**bvalues):
	"""function (targetSide) {
				this.add('-sideend', targetSide, 'Fire Pledge');
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (targetSide) {
				this.add('-sidestart', targetSide, 'Fire Pledge');
			}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move) {
			if (move.sourceEffect === 'waterpledge') {
				move.type = 'Water';
				move.forceSTAB = true;
				move.self = { sideCondition: 'waterpledge' };
			}
			if (move.sourceEffect === 'grasspledge') {
				move.type = 'Fire';
				move.forceSTAB = true;
				move.sideCondition = 'firepledge';
			}
		}
	""" 
	pass

def onPrepareHit(**bvalues):
	"""function (target, source, move) {
			var _a;
			for (var _i = 0, _b = this.queue.list; _i < _b.length; _i++) {
				var action = _b[_i];
				if (!action.move || !((_a = action.pokemon) === null || _a === void 0 ? void 0 : _a.isActive) ||
					action.pokemon.fainted || action.maxMove || action.zmove) {
					continue;
				}
				if (action.pokemon.isAlly(source) && ['grasspledge', 'waterpledge'].includes(action.move.id)) {
					this.queue.prioritizeAction(action, move);
					this.add('-waiting', source, action.pokemon);
					return null;
				}
			}
		}
	""" 
	pass
