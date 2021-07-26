def onHit(**bvalues):
	"""function (target, source) {
			let disallowedMoves = ['chatter', 'sketch', 'struggle'];
			if (source.transformed || !target.lastMove || disallowedMoves.includes(target.lastMove.id) || source.moves.indexOf(target.lastMove.id) >= 0 || target.lastMove.isZ) return false;
			let sketchIndex = source.moves.indexOf('sketch');
			if (sketchIndex < 0) return false;
			let move = this.getMove(target.lastMove);
			let sketchedMove = {
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
