def onAttract(datadic : dict):
	"""function (target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) return False;
		}
	""" 
	pass

def onBoost(datadic : dict):
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

def onDamage(datadic : dict):
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

def onSetAbility(datadic : dict):
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

def onSetStatus(datadic : dict):
	"""function (status, target, source, effect) {
			if (target !== source && target === this.activePokemon && this.activeMove && this.activeMove.flags['contact']) return False;
		}
	""" 
	pass
