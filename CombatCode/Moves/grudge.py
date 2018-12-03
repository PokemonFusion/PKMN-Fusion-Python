def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Grudge');
			}
	""" 
	pass

def onFaint (target, source, effect):
	"""function (target, source, effect) {
				if (!source || source.fainted || !effect) return;
				if (effect.effectType === 'Move' && !effect.isFutureMove && source.lastMove) {
					for (const moveSlot of source.moveSlots) {
						if (moveSlot.id === source.lastMove.id) {
							moveSlot.pp = 0;
							this.add('-activate', source, 'move: Grudge', this.getMove(source.lastMove.id).name);
						}
					}
				}
			}
	""" 
	pass

def onBeforeMove (pokemon):
	"""function (pokemon) {
				this.debug('removing Grudge before attack');
				pokemon.removeVolatile('grudge');
			}
	""" 
	pass