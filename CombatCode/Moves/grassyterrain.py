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
				var weakenedMoves = ['earthquake', 'bulldoze', 'magnitude'];
				if (weakenedMoves.includes(move.id) && defender.isGrounded() && !defender.isSemiInvulnerable()) {
					this.debug('move weakened by grassy terrain');
					return this.chainModify(0.5);
				}
				if (move.type === 'Grass' && attacker.isGrounded()) {
					this.debug('grassy terrain boost');
					return this.chainModify([5325, 4096]);
				}
			}
	""" 
	pass

def onFieldEnd(**bvalues):
	"""function () {
				this.add('-fieldend', 'move: Grassy Terrain');
			}
	""" 
	pass

def onFieldStart(**bvalues):
	"""function (field, source, effect) {
				if ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Ability') {
					this.add('-fieldstart', 'move: Grassy Terrain', '[from] ability: ' + effect, '[of] ' + source);
				}
				else {
					this.add('-fieldstart', 'move: Grassy Terrain');
				}
			}
	""" 
	pass

def onResidual(**bvalues):
	"""function (pokemon) {
				if (pokemon.isGrounded() && !pokemon.isSemiInvulnerable()) {
					this.heal(pokemon.baseMaxhp / 16, pokemon, pokemon);
				}
				else {
					this.debug("Pokemon semi-invuln or not grounded; Grassy Terrain skipped");
				}
			}
	""" 
	pass
