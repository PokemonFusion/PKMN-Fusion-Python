def onAnyBasePower(**bvalues):
	"""function (basePower, target, source, move) {
				if (target !== this.effectState.target && target !== this.effectState.source) {
					return;
				}
				if (source === this.effectState.target && target === this.effectState.source) {
					return;
				}
				if (move.id === 'gust' || move.id === 'twister') {
					return this.chainModify(2);
				}
			}
	""" 
	pass

def onAnyDragOut(**bvalues):
	"""function (pokemon) {
				if (pokemon === this.effectState.target || pokemon === this.effectState.source)
					return false;
			}
	""" 
	pass

def onAnyInvulnerability(**bvalues):
	"""function (target, source, move) {
				if (target !== this.effectState.target && target !== this.effectState.source) {
					return;
				}
				if (source === this.effectState.target && target === this.effectState.source) {
					return;
				}
				if (['gust', 'twister', 'skyuppercut', 'thunder', 'hurricane', 'smackdown', 'thousandarrows'].includes(move.id)) {
					return;
				}
				return false;
			}
	""" 
	pass

def onFaint(**bvalues):
	"""function (target) {
				if (target.volatiles['skydrop'] && target.volatiles['twoturnmove'].source) {
					this.add('-end', target.volatiles['twoturnmove'].source, 'Sky Drop', '[interrupt]');
				}
			}
	""" 
	pass

def onFoeBeforeMove(**bvalues):
	"""function (attacker, defender, move) {
				if (attacker === this.effectState.source) {
					attacker.activeMoveActions--;
					this.debug('Sky drop nullifying.');
					return null;
				}
			}
	""" 
	pass

def onFoeTrapPokemon(**bvalues):
	"""function (defender) {
				if (defender !== this.effectState.source)
					return;
				defender.trapped = true;
			}
	""" 
	pass

def onRedirectTarget(**bvalues):
	"""function (target, source, source2) {
				if (source !== this.effectState.target)
					return;
				if (this.effectState.source.fainted)
					return;
				return this.effectState.source;
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source) {
			if (target.hp)
				this.add('-end', target, 'Sky Drop');
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, source) {
			if (!source.volatiles['skydrop']) {
				move.accuracy = true;
				move.flags.contact = 0;
			}
		}
	""" 
	pass

def onMoveFail(**bvalues):
	"""function (target, source) {
			if (source.volatiles['twoturnmove'] && source.volatiles['twoturnmove'].duration === 1) {
				source.removeVolatile('skydrop');
				source.removeVolatile('twoturnmove');
				if (target === this.effectState.target) {
					this.add('-end', target, 'Sky Drop', '[interrupt]');
				}
			}
		}
	""" 
	pass

def onTry(**bvalues):
	"""function (source, target) {
			return !target.fainted;
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (source.removeVolatile(move.id)) {
				if (target !== source.volatiles['twoturnmove'].source)
					return false;
				if (target.hasType('Flying')) {
					this.add('-immune', target);
					return null;
				}
			}
			else {
				if (target.volatiles['substitute'] || target.isAlly(source)) {
					return false;
				}
				if (target.getWeight() >= 2000) {
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
