def onHit (target, source):
	"""function (target, source) {
			let disallowedMoves = ['chatter', 'mimic', 'sketch', 'struggle', 'transform'];
			if (source.transformed || !target.lastMove || disallowedMoves.includes(target.lastMove.id) || source.moves.indexOf(target.lastMove.id) >= 0 || target.lastMove.isZ) return false;
			let mimicIndex = source.moves.indexOf('mimic');
			if (mimicIndex < 0) return false;
			let move = this.getMove(target.lastMove.id);
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