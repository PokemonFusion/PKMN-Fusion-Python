def onResidual(**bvalues):
	"""function (pokemon) {
				this.damage(pokemon.baseMaxhp / 4);
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon, source) {
				this.add('-start', pokemon, 'Curse', '[of] ' + source);
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source) {
			this.directDamage(source.maxhp / 2, source, source);
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, source, target) {
			if (!source.hasType('Ghost')) {
				move.target = move.nonGhostTarget;
			}
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (!source.hasType('Ghost')) {
				delete move.volatileStatus;
				delete move.onHit;
				move.self = { boosts: { spe: -1, atk: 1, def: 1 } };
			}
			else if (move.volatileStatus && target.volatiles['curse']) {
				return false;
			}
		}
	""" 
	pass
