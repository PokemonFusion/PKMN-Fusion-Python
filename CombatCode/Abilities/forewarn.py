def onStart(**bvalues):
	"""function (pokemon) {
			var warnMoves = [];
			var warnBp = 1;
			for (var _i = 0, _a = pokemon.foes(); _i < _a.length; _i++) {
				var target = _a[_i];
				for (var _b = 0, _c = target.moveSlots; _b < _c.length; _b++) {
					var moveSlot = _c[_b];
					var move = this.dex.moves.get(moveSlot.move);
					var bp = move.basePower;
					if (move.ohko)
						bp = 150;
					if (move.id === 'counter' || move.id === 'metalburst' || move.id === 'mirrorcoat')
						bp = 120;
					if (bp === 1)
						bp = 80;
					if (!bp && move.category !== 'Status')
						bp = 80;
					if (bp > warnBp) {
						warnMoves = [[move, target]];
						warnBp = bp;
					}
					else if (bp === warnBp) {
						warnMoves.push([move, target]);
					}
				}
			}
			if (!warnMoves.length)
				return;
			var _d = this.sample(warnMoves), warnMoveName = _d[0], warnTarget = _d[1];
			this.add('-activate', pokemon, 'ability: Forewarn', warnMoveName, '[of] ' + warnTarget);
		}
	""" 
	pass
