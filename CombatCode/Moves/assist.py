def onHit(**bvalues):
	"""function (target) {
			var noAssist = [
				'assist', 'banefulbunker', 'beakblast', 'belch', 'bestow', 'bounce', 'celebrate', 'chatter', 'circlethrow', 'copycat', 'counter', 'covet', 'destinybond', 'detect', 'dig', 'dive', 'dragontail', 'endure', 'feint', 'fly', 'focuspunch', 'followme', 'helpinghand', 'holdhands', 'kingsshield', 'matblock', 'mefirst', 'metronome', 'mimic', 'mirrorcoat', 'mirrormove', 'naturepower', 'phantomforce', 'protect', 'ragepowder', 'roar', 'shadowforce', 'shelltrap', 'sketch', 'skydrop', 'sleeptalk', 'snatch', 'spikyshield', 'spotlight', 'struggle', 'switcheroo', 'thief', 'transform', 'trick', 'whirlwind',
					];
			var moves = [];
			for (var _i = 0, _a = target.side.pokemon; _i < _a.length; _i++) {
				var pokemon = _a[_i];
				if (pokemon === target)
					continue;
				for (var _b = 0, _c = pokemon.moveSlots; _b < _c.length; _b++) {
					var moveSlot = _c[_b];
					var moveid = moveSlot.id;
					if (noAssist.includes(moveid))
						continue;
					var move = this.dex.moves.get(moveid);
					if (move.isZ || move.isMax) {
						continue;
					}
					moves.push(moveid);
				}
			}
			var randomMove = '';
			if (moves.length)
				randomMove = this.sample(moves);
			if (!randomMove) {
				return false;
			}
			this.actions.useMove(randomMove, target);
		}
	""" 
	pass
