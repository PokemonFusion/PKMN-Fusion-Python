def onHitField (target, source, move):
	"""function (target, source, move) {
			let result = false;
			let message = false;
			for (const side of this.sides) {
				for (const pokemon of side.active) {
					if (pokemon && pokemon.isActive) {
						if (!this.runEvent('Accuracy', pokemon, source, move, true)) {
							this.add('-miss', source, pokemon);
							result = true;
						} else if (this.runEvent('TryHit', pokemon, source, move) === null) {
							result = true;
						} else if (!pokemon.volatiles['perishsong']) {
							pokemon.addVolatile('perishsong');
							this.add('-start', pokemon, 'perish3', '[silent]');
							result = true;
							message = true;
						}
					}
				}
			}
			if (!result) return false;
			if (message) this.add('-fieldactivate', 'move: Perish Song');
		}
	""" 
	pass

def onEnd (target):
	"""function (target) {
				this.add('-start', target, 'perish0');
				target.faint();
			}
	""" 
	pass

def onResidual (pokemon):
	"""function (pokemon) {
				let duration = pokemon.volatiles['perishsong'].duration;
				this.add('-start', pokemon, 'perish' + duration);
			}
	""" 
	pass