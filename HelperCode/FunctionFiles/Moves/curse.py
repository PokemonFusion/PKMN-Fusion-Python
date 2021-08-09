def onResidual (pokemon):
	"""function (pokemon) {
				this.damage(pokemon.baseMaxhp / 4);
			}
	""" 
	pass

def onStart (pokemon, source):
	"""function (pokemon, source) {
				this.add('-start', pokemon, 'Curse', '[of] ' + source);
			}
	""" 
	pass

def onHit (target, source):
	"""function (target, source) {
			this.directDamage(source.maxhp / 2, source, source);
		}
	""" 
	pass

def onModifyMove (move, source, target):
	"""function (move, source, target) {
			if (!source.hasType('Ghost')) {
				move.target = move.nonGhostTarget;
			}
		}
	""" 
	pass

def onTryHit (target, source, move):
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