def onHit(**bvalues):
	"""function (target) {
				if (!target.hp)
					return;
				var move = target.lastMove;
				if (!move || move.isZ)
					return;
				if (move.isMax && move.baseMove)
					move = this.dex.moves.get(move.baseMove);
				var ppDeducted = target.deductPP(move.id, 3);
				if (!ppDeducted)
					return;
				this.add('-activate', target, 'move: Eerie Spell', move.name, ppDeducted);
			}
	""" 
	pass
