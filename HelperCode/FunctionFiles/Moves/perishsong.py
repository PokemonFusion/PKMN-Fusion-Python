def onEnd (target):
	"""function (target) {
				this.add('-start', target, 'perish0');
				target.faint();
			}
	""" 
	pass

def onResidual (pokemon):
	"""function (pokemon) {
				var duration = pokemon.volatiles['perishsong'].duration;
				this.add('-start', pokemon, 'perish' + duration);
			}
	""" 
	pass

def onHitField (target, source, move):
	"""function (target, source, move) {
			var result = false;
			var message = false;
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var pokemon = _a[_i];
				if (this.runEvent('Invulnerability', pokemon, source, move) === false) {
					this.add('-miss', source, pokemon);
					result = true;
				}
				else if (this.runEvent('TryHit', pokemon, source, move) === null) {
					result = true;
				}
				else if (!pokemon.volatiles['perishsong']) {
					pokemon.addVolatile('perishsong');
					this.add('-start', pokemon, 'perish3', '[silent]');
					result = true;
					message = true;
				}
			}
			if (!result)
				return false;
			if (message)
				this.add('-fieldactivate', 'move: Perish Song');
		}
	""" 
	pass