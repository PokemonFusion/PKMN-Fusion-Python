def onHit(**bvalues):
	"""function (target, source) {
			var disallowedMoves = ['chatter', 'sketch', 'struggle'];
			var move = target.lastMove;
			if (source.transformed || !move || source.moves.includes(move.id))
				return false;
			if (disallowedMoves.includes(move.id) || move.isZ || move.isMax)
				return false;
			var sketchIndex = source.moves.indexOf('sketch');
			if (sketchIndex < 0)
				return false;
			var sketchedMove = {
				move: move.name,
				id: move.id,
				pp: move.pp,
				maxpp: move.pp,
				target: move.target,
				disabled: false,
				used: false,
			};
			source.moveSlots[sketchIndex] = sketchedMove;
			source.baseMoveSlots[sketchIndex] = sketchedMove;
			this.add('-activate', source, 'move: Sketch', move.name);
		}
	""" 
	pass
