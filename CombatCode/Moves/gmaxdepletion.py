def onHit(**bvalues):
	"""function (source) {
				for (var _i = 0, _a = source.foes(); _i < _a.length; _i++) {
					var pokemon = _a[_i];
					var move = pokemon.lastMove;
					if (!move || move.isZ)
						continue;
					if (move.isMax && move.baseMove)
						move = this.dex.moves.get(move.baseMove);
					var ppDeducted = pokemon.deductPP(move.id, 2);
					if (ppDeducted) {
						this.add("-activate", pokemon, 'move: G-Max Depletion', move.name, ppDeducted);
						// Don't return here because returning early doesn't trigger
						// activation text for the second Pokemon in doubles
					}
				}
			}
	""" 
	pass
