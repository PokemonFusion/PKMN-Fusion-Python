def basePowerCallback(datadic : dict):
	"""function (pokemon, target, move) {
			// You can't get here unless the pursuit succeeds
			if (target.beingCalledBack) {
				this.debug('Pursuit damage boost');
				return move.basePower * 2;
			}
			return move.basePower;
		}
	""" 
	pass

def beforeTurnCallback(datadic : dict):
	"""function (pokemon) {
			for (const side of this.sides) {
				if (side === pokemon.side) continue;
				side.addSideCondition('pursuit', pokemon);
				if (!side.sideConditions['pursuit'].sources) {
					side.sideConditions['pursuit'].sources = [];
				}
				side.sideConditions['pursuit'].sources.push(pokemon);
			}
		}
	""" 
	pass

def onModifyMove(datadic : dict):
	"""function (move, source, target) {
			if (target && target.beingCalledBack) move.accuracy = true;
		}
	""" 
	pass

def onTryHit(datadic : dict):
	"""function (target, pokemon) {
			target.side.removeSideCondition('pursuit');
		}
	""" 
	pass

def onBeforeSwitchOut(datadic : dict):
	"""function (pokemon) {
				this.debug('Pursuit start');
				let alreadyAdded = false;
				for (const source of this.effectData.sources) {
					if (!this.cancelMove(source) || !source.hp) continue;
					if (!alreadyAdded) {
						this.add('-activate', pokemon, 'move: Pursuit');
						alreadyAdded = true;
					}
					// Run through each action in queue to check if the Pursuit user is supposed to Mega Evolve this turn.
					// If it is, then Mega Evolve before moving.
					if (source.canMegaEvo || source.canUltraBurst) {
						for (const [actionIndex, action] of this.queue.entries()) {
							if (action.pokemon === source && action.choice === 'megaEvo') {
								this.runMegaEvo(source);
								this.queue.splice(actionIndex, 1);
								break;
							}
						}
					}
					this.runMove('pursuit', source, this.getTargetLoc(pokemon, source));
				}
			}
	""" 
	pass
