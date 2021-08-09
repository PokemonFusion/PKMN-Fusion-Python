def onAnyPrepareHit(**bvalues):
	"""function (source, target, move) {
				var snatchUser = this.effectState.source;
				if (snatchUser.isSkyDropped())
					return;
				if (!move || move.isZ || move.isMax || !move.flags['snatch'] || move.sourceEffect === 'snatch') {
					return;
				}
				snatchUser.removeVolatile('snatch');
				this.add('-activate', snatchUser, 'move: Snatch', '[of] ' + source);
				this.actions.useMove(move.id, snatchUser);
				return null;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.add('-singleturn', pokemon, 'Snatch');
			}
	""" 
	pass
