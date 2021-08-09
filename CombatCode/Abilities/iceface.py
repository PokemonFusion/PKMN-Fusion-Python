def onStart(**bvalues):
	"""function (pokemon) {
			if (this.field.isWeather('hail') && pokemon.species.id === 'eiscuenoice' && !pokemon.transformed) {
				this.add('-activate', pokemon, 'ability: Ice Face');
				this.effectState.busted = False;
				pokemon.formeChange('Eiscue', this.effect, True);
			}
		}
	""" 
	pass

def onDamage(**bvalues):
	"""function (damage, target, source, effect) {
			if (effect && effect.effectType === 'Move' && effect.category === 'Physical' &&
				target.species.id === 'eiscue' && !target.transformed) {
				this.add('-activate', target, 'ability: Ice Face');
				this.effectState.busted = True;
				return 0;
			}
		}
	""" 
	pass

def onCriticalHit(**bvalues):
	"""function (target, type, move) {
			if (!target)
				return;
			if (move.category !== 'Physical' || target.species.id !== 'eiscue' || target.transformed)
				return;
			if (target.volatiles['substitute'] && !(move.flags['authentic'] || move.infiltrates))
				return;
			if (!target.runImmunity(move.type))
				return;
			return False;
		}
	""" 
	pass

def onEffectiveness(**bvalues):
	"""function (typeMod, target, type, move) {
			if (!target)
				return;
			if (move.category !== 'Physical' || target.species.id !== 'eiscue' || target.transformed)
				return;
			var hitSub = target.volatiles['substitute'] && !move.flags['authentic'] && !(move.infiltrates && this.gen >= 6);
			if (hitSub)
				return;
			if (!target.runImmunity(move.type))
				return;
			return 0;
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.species.id === 'eiscue' && this.effectState.busted) {
				pokemon.formeChange('Eiscue-Noice', this.effect, True);
			}
		}
	""" 
	pass

def onAnyWeatherStart(**bvalues):
	"""function () {
			var pokemon = this.effectState.target;
			if (!pokemon.hp)
				return;
			if (this.field.isWeather('hail') && pokemon.species.id === 'eiscuenoice' && !pokemon.transformed) {
				this.add('-activate', pokemon, 'ability: Ice Face');
				this.effectState.busted = False;
				pokemon.formeChange('Eiscue', this.effect, True);
			}
		}
	""" 
	pass
