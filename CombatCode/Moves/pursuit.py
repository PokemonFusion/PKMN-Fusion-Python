def basePowerCallback(**bvalues):
	"""function (pokemon, target, move) {
			// You can't get here unless the pursuit succeeds
			if (target.beingCalledBack || target.switchFlag) {
				this.debug('Pursuit damage boost');
				return move.basePower * 2;
			}
			return move.basePower;
		}
	""" 
	pass

def beforeTurnCallback(**bvalues):
	"""function (pokemon) {
			for (var _i = 0, _a = this.sides; _i < _a.length; _i++) {
				var side = _a[_i];
				if (side.hasAlly(pokemon))
					continue;
				side.addSideCondition('pursuit', pokemon);
				var data = side.getSideConditionData('pursuit');
				if (!data.sources) {
					data.sources = [];
				}
				data.sources.push(pokemon);
			}
		}
	""" 
	pass

def onBeforeSwitchOut(**bvalues):
	"""function (pokemon) {
				this.debug('Pursuit start');
				var alreadyAdded = false;
				pokemon.removeVolatile('destinybond');
				for (var _i = 0, _a = this.effectState.sources; _i < _a.length; _i++) {
					var source = _a[_i];
					if (!this.queue.cancelMove(source) || !source.hp)
						continue;
					if (!alreadyAdded) {
						this.add('-activate', pokemon, 'move: Pursuit');
						alreadyAdded = true;
					}
					// Run through each action in queue to check if the Pursuit user is supposed to Mega Evolve this turn.
					// If it is, then Mega Evolve before moving.
					if (source.canMegaEvo || source.canUltraBurst) {
						for (var _b = 0, _c = this.queue.entries(); _b < _c.length; _b++) {
							var _d = _c[_b], actionIndex = _d[0], action = _d[1];
							if (action.pokemon === source && action.choice === 'megaEvo') {
								this.actions.runMegaEvo(source);
								this.queue.list.splice(actionIndex, 1);
								break;
							}
						}
					}
					this.actions.runMove('pursuit', source, source.getLocOf(pokemon));
				}
			}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, source, target) {
			if ((target === null || target === void 0 ? void 0 : target.beingCalledBack) || (target === null || target === void 0 ? void 0 : target.switchFlag))
				move.accuracy = true;
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, pokemon) {
			target.side.removeSideCondition('pursuit');
		}
	""" 
	pass
