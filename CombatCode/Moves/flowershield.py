def onHitField(**bvalues):
	"""function (t, source, move) {
			var targets = [];
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var pokemon = _a[_i];
				if (pokemon.hasType('Grass') &&
					(!pokemon.volatiles['maxguard'] ||
						this.runEvent('TryHit', pokemon, source, move))) {
					// This move affects every Grass-type Pokemon in play.
					targets.push(pokemon);
				}
			}
			var success = false;
			for (var _b = 0, targets_1 = targets; _b < targets_1.length; _b++) {
				var target = targets_1[_b];
				success = this.boost({ def: 1 }, target, source, move) || success;
			}
			return success;
		}
	""" 
	pass
