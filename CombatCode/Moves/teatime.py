def onHitField(**bvalues):
	"""function (target, source, move) {
			var result = false;
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var active = _a[_i];
				if (this.runEvent('Invulnerability', active, source, move) === false) {
					this.add('-miss', source, active);
					result = true;
				}
				else if (this.runEvent('TryHit', active, source, move)) {
					var item = active.getItem();
					if (active.hp && item.isBerry) {
						// bypasses Unnerve
						active.eatItem(true);
						result = true;
					}
				}
			}
			return result;
		}
	""" 
	pass
