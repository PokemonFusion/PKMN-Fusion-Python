def onHit (target, source, effect):
	"""function (target, source, effect) {
			var moves = [];
			for (var id in exports.Moves) {
				var move = exports.Moves[id];
				if (move.realMove)
					continue;
				if (move.isZ || move.isMax || move.isNonstandard)
					continue;
				if (effect.noMetronome.includes(move.name))
					continue;
				if (this.dex.moves.get(id).gen > this.gen)
					continue;
				moves.push(move);
			}
			var randomMove = '';
			if (moves.length) {
				moves.sort(function (a, b) { return a.num - b.num; });
				randomMove = this.sample(moves).name;
			}
			if (!randomMove) {
				return false;
			}
			this.actions.useMove(randomMove, target);
		}
	""" 
	pass