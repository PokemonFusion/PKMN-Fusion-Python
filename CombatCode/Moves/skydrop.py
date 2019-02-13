def onModifyMove(datadic : dict):
	"""function (move, source) {
			if (!source.volatiles['skydrop']) {
				move.accuracy = true;
				move.flags.contact = 0;
			}
		}
	""" 
	pass

def onMoveFail(datadic : dict):
	"""function (target, source) {
			if (source.volatiles['twoturnmove'] && source.volatiles['twoturnmove'].duration === 1) {
				source.removeVolatile('skydrop');
				source.removeVolatile('twoturnmove');
				this.add('-end', target, 'Sky Drop', '[interrupt]');
			}
		}
	""" 
	pass

def onTryHit(datadic : dict):
	"""function (target, source, move) {
			if (target.fainted) return false;
			if (source.removeVolatile(move.id)) {
				if (target !== source.volatiles['twoturnmove'].source) return false;

				if (target.hasType('Flying')) {
					this.add('-immune', target);
					return null;
				}
			} else {
				if (target.volatiles['substitute'] || target.side === source.side) {
					return false;
				}
				if (target.getWeight() >= 200) {
					this.add('-fail', target, 'move: Sky Drop', '[heavy]');
					return null;
				}

				this.add('-prepare', source, move.name, target);
				source.addVolatile('twoturnmove', target);
				return null;
			}
		}
	""" 
	pass

def onHit(datadic : dict):
	"""function (target, source) {
			this.add('-end', target, 'Sky Drop');
		}
	""" 
	pass

def onAnyDragOut(datadic : dict):
	"""function (pokemon) {
				if (pokemon === this.effectData.target || pokemon === this.effectData.source) return false;
			}
	""" 
	pass

def onFoeTrapPokemon(datadic : dict):
	"""function (defender) {
				if (defender !== this.effectData.source) return;
				defender.trapped = true;
			}
	""" 
	pass

def onFoeBeforeMove(datadic : dict):
	"""function (attacker, defender, move) {
				if (attacker === this.effectData.source) {
					this.effectData.source.activeTurns--;
					this.debug('Sky drop nullifying.');
					return null;
				}
			}
	""" 
	pass

def onRedirectTarget(datadic : dict):
	"""function (target, source, source2) {
				if (source !== this.effectData.target) return;
				if (this.effectData.source.fainted) return;
				return this.effectData.source;
			}
	""" 
	pass

def onAnyTryImmunity(datadic : dict):
	"""function (target, source, move) {
				if (target !== this.effectData.target && target !== this.effectData.source) {
					return;
				}
				if (source === this.effectData.target && target === this.effectData.source) {
					return;
				}
				if (move.id === 'gust' || move.id === 'twister') {
					return;
				}
				if (move.id === 'skyuppercut' || move.id === 'thunder' || move.id === 'hurricane' || move.id === 'smackdown' || move.id === 'thousandarrows' || move.id === 'helpinghand') {
					return;
				}
				if (source.hasAbility('noguard') || target.hasAbility('noguard')) {
					return;
				}
				if (source.volatiles['lockon'] && target === source.volatiles['lockon'].source) return;
				return false;
			}
	""" 
	pass

def onAnyBasePower(datadic : dict):
	"""function (basePower, target, source, move) {
				if (target !== this.effectData.target && target !== this.effectData.source) {
					return;
				}
				if (source === this.effectData.target && target === this.effectData.source) {
					return;
				}
				if (move.id === 'gust' || move.id === 'twister') {
					return this.chainModify(2);
				}
			}
	""" 
	pass

def onFaint(datadic : dict):
	"""function (target) {
				if (target.volatiles['skydrop'] && target.volatiles['twoturnmove'].source) {
					this.add('-end', target.volatiles['twoturnmove'].source, 'Sky Drop', '[interrupt]');
				}
			}
	""" 
	pass
