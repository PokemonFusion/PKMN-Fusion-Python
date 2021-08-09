def onDamagingHit(**bvalues):
	"""function (damage, target, source, move) {
			var activated = False;
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var pokemon = _a[_i];
				if (pokemon === target || pokemon.fainted)
					continue;
				if (!activated) {
					this.add('-ability', target, 'Cotton Down');
					activated = True;
				}
				this.boost({ spe: -1 }, pokemon, target, null, True);
			}
		}
	""" 
	pass
