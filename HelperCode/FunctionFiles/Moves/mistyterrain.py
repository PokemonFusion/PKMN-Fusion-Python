def durationCallback (source, effect):
	"""function (source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasItem('terrainextender')) {
					return 8;
				}
				return 5;
			}
	""" 
	pass

def onBasePower (basePower, attacker, defender, move):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Dragon' && defender.isGrounded() && !defender.isSemiInvulnerable()) {
					this.debug('misty terrain weaken');
					return this.chainModify(0.5);
				}
			}
	""" 
	pass

def onFieldEnd ():
	"""function () {
				this.add('-fieldend', 'Misty Terrain');
			}
	""" 
	pass

def onFieldStart (field, source, effect):
	"""function (field, source, effect) {
				if ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Ability') {
					this.add('-fieldstart', 'move: Misty Terrain', '[from] ability: ' + effect, '[of] ' + source);
				}
				else {
					this.add('-fieldstart', 'move: Misty Terrain');
				}
			}
	""" 
	pass

def onSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
				if (!target.isGrounded() || target.isSemiInvulnerable())
					return;
				if (effect && (effect.status || effect.id === 'yawn')) {
					this.add('-activate', target, 'move: Misty Terrain');
				}
				return false;
			}
	""" 
	pass

def onTryAddVolatile (status, target, source, effect):
	"""function (status, target, source, effect) {
				if (!target.isGrounded() || target.isSemiInvulnerable())
					return;
				if (status.id === 'confusion') {
					if (effect.effectType === 'Move' && !effect.secondaries)
						this.add('-activate', target, 'move: Misty Terrain');
					return null;
				}
			}
	""" 
	pass