def onAttract (target, source, effect):
	"""function (target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) return False;
		}
	""" 
	pass

def onBoost (boost, target, source, effect):
	"""function (boost, target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) {
				if (effect && effect.effectType === 'Ability') {
					// Ability activation always happens for boosts
					this.add('-activate', target, 'item: Protective Pads');
				}
				return False;
			}
		}
	""" 
	pass

def onDamage (damage, target, source, effect):
	"""function (damage, target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) {
				if (effect && effect.effectType === 'Ability') {
					this.add('-activate', source, effect.fullname);
					this.add('-activate', target, 'item: Protective Pads');
				}
				return False;
			}
		}
	""" 
	pass

def onSetAbility (ability, target, source, effect):
	"""function (ability, target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) {
				if (effect && effect.effectType === 'Ability') {
					this.add('-activate', source, effect.fullname);
					this.add('-activate', target, 'item: Protective Pads');
				}
				return False;
			}
		}
	""" 
	pass

def onSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) return False;
		}
	""" 
	pass