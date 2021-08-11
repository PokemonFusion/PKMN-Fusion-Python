def durationCallback(**bvalues):
	"""function (source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasItem('terrainextender')) {
					return 8;
				}
				return 5;
			}
	""" 
	pass

def onBasePower(**bvalues):
	"""function (basePower, attacker, defender, move) {
				if (move.type === 'Psychic' && attacker.isGrounded() && !attacker.isSemiInvulnerable()) {
					this.debug('psychic terrain boost');
					return this.chainModify([5325, 4096]);
				}
			}
	""" 
	pass

def onFieldEnd(**bvalues):
	"""function () {
				this.add('-fieldend', 'move: Psychic Terrain');
			}
	""" 
	pass

def onFieldStart(**bvalues):
	"""function (field, source, effect) {
				if ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Ability') {
					this.add('-fieldstart', 'move: Psychic Terrain', '[from] ability: ' + effect, '[of] ' + source);
				}
				else {
					this.add('-fieldstart', 'move: Psychic Terrain');
				}
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, effect) {
				if (effect && (effect.priority <= 0.1 || effect.target === 'self')) {
					return;
				}
				if (target.isSemiInvulnerable() || target.isAlly(source))
					return;
				if (!target.isGrounded()) {
					var baseMove = this.dex.moves.get(effect.id);
					if (baseMove.priority > 0) {
						this.hint("Psychic Terrain doesn't affect Pokemon immune to Ground.");
					}
					return;
				}
				this.add('-activate', target, 'move: Psychic Terrain');
				return null;
			}
	""" 
	pass
