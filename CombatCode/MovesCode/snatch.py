def onStart (pokemon):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'Snatch');
			}
	""" 
	pass

def onAnyTryMove (source, target, move):
	"""function (source, target, move) {
				let snatchUser = this.effectData.source;
				if (snatchUser.isSkyDropped()) return;
				if (move && !move.isZ && move.flags['snatch'] && move.sourceEffect !== 'snatch') {
					snatchUser.removeVolatile('snatch');
					this.add('-activate', snatchUser, 'move: Snatch', '[of] ' + source);
					this.useMove(move.id, snatchUser);
					return null;
				}
			}
	""" 
	pass