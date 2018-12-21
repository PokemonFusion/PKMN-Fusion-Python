def onStart (target):
	"""function (target) {
				this.add('-singleturn', target, 'Powder');
			}
	""" 
	pass

def onTryMove (pokemon, target, move):
	"""function (pokemon, target, move) {
				if (move.type === 'Fire') {
					this.add('-activate', pokemon, 'move: Powder');
					this.damage(this.clampIntRange(Math.round(pokemon.maxhp / 4), 1));
					return false;
				}
			}
	""" 
	pass