def onHit(**bvalues):
	"""function (target, source) {
			var disallowedMoves = ['chatter', 'mimic', 'sketch', 'struggle', 'transform'];
			var move = target.lastMove;
			if (source.transformed || !move || disallowedMoves.includes(move.id) || source.moves.includes(move.id)) {
				return false;
			}
			if (move.isZ || move.isMax)
				return false;
			var mimicIndex = source.moves.indexOf('mimic');
			if (mimicIndex < 0)
				return false;
			source.moveSlots[mimicIndex] = {
				move: move.name,
				id: move.id,
				pp: move.pp,
				maxpp: move.pp,
				target: move.target,
				disabled: false,
				used: false,
				virtual: true,
			};
			this.add('-start', source, 'Mimic', move.name);
		}
	""" 
	pass
