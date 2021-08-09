def onSideStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'move: G-Max Steelsurge');
			}
	""" 
	pass

def onSwitchIn(**bvalues):
	"""function (pokemon) {
				if (pokemon.hasItem('heavydutyboots'))
					return;
				// Ice Face and Disguise correctly get typed damage from Stealth Rock
				// because Stealth Rock bypasses Substitute.
				// They don't get typed damage from Steelsurge because Steelsurge doesn't,
				// so we're going to test the damage of a Steel-type Stealth Rock instead.
				var steelHazard = this.dex.getActiveMove('Stealth Rock');
				steelHazard.type = 'Steel';
				var typeMod = this.clampIntRange(pokemon.runEffectiveness(steelHazard), -6, 6);
				this.damage(pokemon.maxhp * Math.pow(2, typeMod) / 8);
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (source) {
				for (var _i = 0, _a = source.side.foeSidesWithConditions(); _i < _a.length; _i++) {
					var side = _a[_i];
					side.addSideCondition('gmaxsteelsurge');
				}
			}
	""" 
	pass
