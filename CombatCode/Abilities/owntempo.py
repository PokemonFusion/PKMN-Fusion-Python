def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.volatiles['confusion']) {
				this.add('-activate', pokemon, 'ability: Own Tempo');
				pokemon.removeVolatile('confusion');
			}
		}
	""" 
	pass

def onTryAddVolatile(**bvalues):
	"""function (status, pokemon) {
			if (status.id === 'confusion') return null;
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
			if (move && move.volatileStatus === 'confusion') {
				this.add('-immune', target, 'confusion', '[from] ability: Own Tempo');
			}
		}
	""" 
	pass
