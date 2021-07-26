def onStart(**bvalues):
	"""function (target) {
				this.add('-start', target, 'move: Leech Seed');
			}
	""" 
	pass

def onResidual(**bvalues):
	"""function (pokemon) {
				let target = this.effectData.source.side.active[pokemon.volatiles['leechseed'].sourcePosition];
				if (!target || target.fainted || target.hp <= 0) {
					this.debug('Nothing to leech into');
					return;
				}
				let damage = this.damage(pokemon.maxhp / 8, pokemon, target);
				if (damage) {
					this.heal(damage, target, pokemon);
				}
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target) {
			if (target.hasType('Grass')) {
				this.add('-immune', target);
				return null;
			}
		}
	""" 
	pass
