def onResidual(**bvalues):
	"""function (pokemon) {
				var target = this.getAtSlot(pokemon.volatiles['leechseed'].sourceSlot);
				if (!target || target.fainted || target.hp <= 0) {
					this.debug('Nothing to leech into');
					return;
				}
				var damage = this.damage(pokemon.baseMaxhp / 8, pokemon, target);
				if (damage) {
					this.heal(damage, target, pokemon);
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'move: Leech Seed');
			}
	""" 
	pass

def onTryImmunity(**bvalues):
	"""function (target) {
			return !target.hasType('Grass');
		}
	""" 
	pass
