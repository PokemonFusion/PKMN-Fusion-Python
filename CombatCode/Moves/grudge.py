def onBeforeMove(**bvalues):
	"""function (pokemon) {
				this.debug('removing Grudge before attack');
				pokemon.removeVolatile('grudge');
			}
	""" 
	pass

def onFaint(**bvalues):
	"""function (target, source, effect) {
				if (!source || source.fainted || !effect)
					return;
				if (effect.effectType === 'Move' && !effect.isFutureMove && source.lastMove) {
					var move = source.lastMove;
					if (move.isMax && move.baseMove)
						move = this.dex.moves.get(move.baseMove);
					for (var _i = 0, _a = source.moveSlots; _i < _a.length; _i++) {
						var moveSlot = _a[_i];
						if (moveSlot.id === move.id) {
							moveSlot.pp = 0;
							this.add('-activate', source, 'move: Grudge', move.name);
						}
					}
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Grudge');
			}
	""" 
	pass
