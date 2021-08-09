def onAfterSubDamage(**bvalues):
	"""function (damage, target, source, move) {
			if (!source.isAlly(target))
				this.hint(move.category + " Shell Side Arm");
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (target, source, move) {
			// Shell Side Arm normally reveals its category via animation on cart, but doesn't play either custom animation against allies
			if (!source.isAlly(target))
				this.hint(move.category + " Shell Side Arm");
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, pokemon, target) {
			if (!target)
				return;
			var atk = pokemon.getStat('atk', false, true);
			var spa = pokemon.getStat('spa', false, true);
			var def = target.getStat('def', false, true);
			var spd = target.getStat('spd', false, true);
			var physical = Math.floor(Math.floor(Math.floor(Math.floor(2 * pokemon.level / 5 + 2) * 90 * atk) / def) / 50);
			var special = Math.floor(Math.floor(Math.floor(Math.floor(2 * pokemon.level / 5 + 2) * 90 * spa) / spd) / 50);
			if (physical > special || (physical === special && this.random(2) === 0)) {
				move.category = 'Physical';
				move.flags.contact = 1;
			}
		}
	""" 
	pass

def onPrepareHit(**bvalues):
	"""function (target, source, move) {
			if (!source.isAlly(target)) {
				this.attrLastMove('[anim] Shell Side Arm ' + move.category);
			}
		}
	""" 
	pass
