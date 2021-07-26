def onHitField(**bvalues):
	"""function (target, source) {
			let targets = [];
			let anyAirborne = false;
			for (const side of this.sides) {
				for (const pokemon of side.active) {
					if (!pokemon || !pokemon.isActive) continue;
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
			}
			if (!targets.length && !anyAirborne) return false; // Fails when there are no grounded Grass types or airborne Pokemon
			for (const pokemon of targets) {
				this.boost({atk: 1, spa: 1}, pokemon, source);
			}
		}
	""" 
	pass
