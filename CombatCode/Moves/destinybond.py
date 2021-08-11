def onBeforeMove(**bvalues):
	"""function (pokemon, target, move) {
				if (move.id === 'destinybond')
					return;
				this.debug('removing Destiny Bond before attack');
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass

def onFaint(**bvalues):
	"""function (target, source, effect) {
				if (!source || !effect || target.isAlly(source))
					return;
				if (effect.effectType === 'Move' && !effect.isFutureMove) {
					if (source.volatiles['dynamax']) {
						this.add('-hint', "Dynamaxed Pokemon are immune to Destiny Bond.");
						return;
					}
					this.add('-activate', target, 'move: Destiny Bond');
					source.faint();
				}
			}
	"""
	pass

def onMoveAborted(**bvalues):
	"""function (pokemon, target, move) {
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Destiny Bond');
			}
	""" 
	pass

def onPrepareHit(**bvalues):
	"""function (pokemon) {
			return !pokemon.removeVolatile('destinybond');
		}
	""" 
	pass
