def onAttract(**bvalues):
	"""function (target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) return False;
		}
	""" 
	pass

def onBoost(**bvalues):
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

def onDamage(**bvalues):
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

def onSetAbility(**bvalues):
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

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) return False;
		}
	""" 
	pass
