def onUpdate (pokemon):
	"""function (pokemon) {
			if (pokemon.volatiles['confusion']) {
				this.add('-activate', pokemon, 'ability: Own Tempo');
				pokemon.removeVolatile('confusion');
			}
		}
	""" 
	pass

def onTryAddVolatile (status, pokemon):
	"""function (status, pokemon) {
			if (status.id === 'confusion')
				return null;
		}
	""" 
	pass

def onHit (target, source, move):
	"""function (target, source, move) {
			if ((move === null || move === void 0 ? void 0 : move.volatileStatus) === 'confusion') {
				this.add('-immune', target, 'confusion', '[from] ability: Own Tempo');
			}
		}
	""" 
	pass

def onBoost (boost, target, source, effect):
	"""function (boost, target, source, effect) {
			if (effect.id === 'intimidate') {
				delete boost.atk;
				this.add('-fail', target, 'unboost', 'Attack', '[from] ability: Own Tempo', '[of] ' + target);
			}
		}
	""" 
	pass