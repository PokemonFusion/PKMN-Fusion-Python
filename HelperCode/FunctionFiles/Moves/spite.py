def onHit (target):
	"""function (target) {
			var move = target.lastMove;
			if (!move || move.isZ)
				return false;
			if (move.isMax && move.baseMove)
				move = this.dex.moves.get(move.baseMove);
			var ppDeducted = target.deductPP(move.id, 4);
			if (!ppDeducted)
				return false;
			this.add("-activate", target, 'move: Spite', move.name, ppDeducted);
		}
	""" 
	pass