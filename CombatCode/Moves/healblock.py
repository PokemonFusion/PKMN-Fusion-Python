def durationCallback (target, source, effect):
	"""function (target, source, effect) {
				if (source && source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.add('-start', pokemon, 'move: Heal Block');
			}
	""" 
	pass

def onDisableMove (pokemon):
	"""function (pokemon) {
				for (const moveSlot of pokemon.moveSlots) {
					if (this.getMove(moveSlot.id).flags['heal']) {
						pokemon.disableMove(moveSlot.id);
					}
				}
			}
	""" 
	pass

def onBeforeMove (pokemon, target, move):
	"""function (pokemon, target, move) {
				if (move.flags['heal'] && !move.isZ) {
					this.add('cant', pokemon, 'move: Heal Block', move);
					return false;
				}
			}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Heal Block');
			}
	""" 
	pass

def onTryHeal (damage, target, source, effect):
	"""function (damage, target, source, effect) {
				if ((effect && effect.id === 'zpower') || this.effectData.isZ) return damage;
				return false;
			}
	""" 
	pass