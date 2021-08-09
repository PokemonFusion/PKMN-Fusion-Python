def onDamagingHit(**bvalues):
	"""function (damage, target, source, move) {
			if (!this.checkMoveMakesContact(move, source, target))
				return;
			var announced = False;
			for (var _i = 0, _a = [target, source]; _i < _a.length; _i++) {
				var pokemon = _a[_i];
				if (pokemon.volatiles['perishsong'])
					continue;
				if (!announced) {
					this.add('-ability', target, 'Perish Body');
					announced = True;
				}
				pokemon.addVolatile('perishsong');
			}
		}
	""" 
	pass
