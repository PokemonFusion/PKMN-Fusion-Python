def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singlemove', pokemon, 'Rage');
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
				if (target !== source && move.category !== 'Status') {
					this.boost({atk: 1});
				}
			}
	""" 
	pass

def onBeforeMove(**bvalues):
	"""function (pokemon) {
				this.debug('removing Rage before attack');
				pokemon.removeVolatile('rage');
			}
	""" 
	pass
