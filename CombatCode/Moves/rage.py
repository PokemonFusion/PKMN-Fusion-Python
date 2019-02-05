def onStart(datadic : dict):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Rage');
			}
	""" 
	pass

def onHit(datadic : dict):
	"""function (target, source, move) {
				if (target !== source && move.category !== 'Status') {
					this.boost({atk: 1});
				}
			}
	""" 
	pass

def onBeforeMove(datadic : dict):
	"""function (pokemon) {
				this.debug('removing Rage before attack');
				pokemon.removeVolatile('rage');
			}
	""" 
	pass
