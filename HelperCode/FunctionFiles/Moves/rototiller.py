def onHitField (target, source):
	"""function (target, source) {
			var targets = [];
			var anyAirborne = false;
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var pokemon = _a[_i];
				if (!pokemon.runImmunity('Ground')) {
					this.add('-immune', pokemon);
					anyAirborne = true;
					continue;
				}
				if (pokemon.hasType('Grass')) {
					// This move affects every grounded Grass-type Pokemon in play.
					targets.push(pokemon);
				}
			}
			if (!targets.length && !anyAirborne)
				return false; // Fails when there are no grounded Grass types or airborne Pokemon
			for (var _b = 0, targets_4 = targets; _b < targets_4.length; _b++) {
				var pokemon = targets_4[_b];
				this.boost({ atk: 1, spa: 1 }, pokemon, source);
			}
		}
	""" 
	pass