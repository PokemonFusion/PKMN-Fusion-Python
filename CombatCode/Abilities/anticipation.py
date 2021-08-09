def onStart(**bvalues):
	"""function (pokemon) {
			for (var _i = 0, _a = pokemon.foes(); _i < _a.length; _i++) {
				var target = _a[_i];
				for (var _b = 0, _c = target.moveSlots; _b < _c.length; _b++) {
					var moveSlot = _c[_b];
					var move = this.dex.moves.get(moveSlot.move);
					if (move.category === 'Status')
						continue;
					var moveType = move.id === 'hiddenpower' ? target.hpType : move.type;
					if (this.dex.getImmunity(moveType, pokemon) && this.dex.getEffectiveness(moveType, pokemon) > 0 ||
						move.ohko) {
						this.add('-ability', pokemon, 'Anticipation');
						return;
					}
				}
			}
		}
	""" 
	pass
