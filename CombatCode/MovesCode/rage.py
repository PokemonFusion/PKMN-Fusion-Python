def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Rage');
			}
	""" 
	pass

def onHit (target, source, move):
	"""function (target, source, move) {
				if (target !== source && move.category !== 'Status') {
					this.boost({atk: 1});
				}
			}
	""" 
	pass

def onBeforeMove (pokemon):
	"""function (pokemon) {
				this.debug('removing Rage before attack');
				pokemon.removeVolatile('rage');
			}
	""" 
	pass