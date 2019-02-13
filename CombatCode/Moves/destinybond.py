def onPrepareHit(datadic : dict):
	"""function (pokemon) {
			return !pokemon.removeVolatile('destinybond');
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Destiny Bond');
			}
	""" 
	pass

def onFaint(datadic : dict):
	"""function (target, source, effect) {
				if (!source || !effect || target.side === source.side) return;
				if (effect.effectType === 'Move' && !effect.isFutureMove) {
					this.add('-activate', target, 'move: Destiny Bond');
					source.faint();
				}
			}
	""" 
	pass

def onBeforeMove(datadic : dict):
	"""function (pokemon, target, move) {
				if (move.id === 'destinybond') return;
				this.debug('removing Destiny Bond before attack');
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass

def onMoveAborted(datadic : dict):
	"""function (pokemon, target, move) {
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass

def onBeforeSwitchOut(datadic : dict):
	"""function (pokemon) {
				pokemon.removeVolatile('destinybond');
			}
	""" 
	pass
