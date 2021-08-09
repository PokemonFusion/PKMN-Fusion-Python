def basePowerCallback(**bvalues):
	"""function (target, source, move) {
			if (['waterpledge', 'firepledge'].includes(move.sourceEffect)) {
				this.add('-combine');
				return 150;
			}
			return 80;
		}
	""" 
	pass

def onModifySpe(**bvalues):
	"""function (spe, pokemon) {
				return this.chainModify(0.25);
			}
	""" 
	pass

def onSideEnd(**bvalues):
	"""function (targetSide) {
				this.add('-sideend', targetSide, 'Grass Pledge');
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (targetSide) {
				this.add('-sidestart', targetSide, 'Grass Pledge');
			}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move) {
			if (move.sourceEffect === 'waterpledge') {
				move.type = 'Grass';
				move.forceSTAB = true;
				move.sideCondition = 'grasspledge';
			}
			if (move.sourceEffect === 'firepledge') {
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
				if (action.pokemon.isAlly(source) && ['waterpledge', 'firepledge'].includes(action.move.id)) {
					this.queue.prioritizeAction(action, move);
					this.add('-waiting', source, action.pokemon);
					return null;
				}
			}
		}
	""" 
	pass
