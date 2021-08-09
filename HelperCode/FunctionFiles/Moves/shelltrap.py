def beforeTurnCallback (pokemon):
	"""function (pokemon) {
			pokemon.addVolatile('shelltrap');
		}
	""" 
	pass

def onHit (pokemon, source, move):
	"""function (pokemon, source, move) {
				if (!pokemon.isAlly(source) && move.category === 'Physical') {
					pokemon.volatiles['shelltrap'].gotHit = true;
					var action = this.queue.willMove(pokemon);
					if (action) {
						this.queue.prioritizeAction(action);
					}
				}
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'move: Shell Trap');
			}
	""" 
	pass

def onTryMove (pokemon):
	"""function (pokemon) {
			var _a;
			if (!((_a = pokemon.volatiles['shelltrap']) === null || _a === void 0 ? void 0 : _a.gotHit)) {
				this.attrLastMove('[still]');
				this.add('cant', pokemon, 'Shell Trap', 'Shell Trap');
				return null;
			}
		}
	""" 
	pass