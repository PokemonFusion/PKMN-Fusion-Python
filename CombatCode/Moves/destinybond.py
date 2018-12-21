def onPrepareHit (pokemon):
	"""function (pokemon) {
			return !pokemon.removeVolatile('destinybond');
		}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Destiny Bond');
			}
	""" 
	pass

def onFaint (target, source, effect):
	"""function (target, source, effect) {
				if (!source || !effect || target.side === source.side) return;
				if (effect.effectType === 'Move' && !effect.isFutureMove) {
					this.add('-activate', target, 'move: Destiny Bond');
					source.faint();
				}
			}
	""" 
	pass

def onBeforeMove (pokemon, target, move):
	"""function (pokemon, target, move) {
				if (move.id === 'destinybond') return;
				this.debug('removing Destiny Bond before attack');
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass

def onMoveAborted (pokemon, target, move):
	"""function (pokemon, target, move) {
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass

def onBeforeSwitchOut (pokemon):
	"""function (pokemon) {
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass