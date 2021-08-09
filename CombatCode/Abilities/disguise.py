def onDamage(**bvalues):
	"""function (damage, target, source, effect) {
			if (effect && effect.effectType === 'Move' &&
				['mimikyu', 'mimikyutotem'].includes(target.species.id) && !target.transformed) {
				this.add('-activate', target, 'ability: Disguise');
				this.effectState.busted = True;
				return 0;
			}
		}
	""" 
	pass

def onCriticalHit(**bvalues):
	"""function (target, source, move) {
			if (!target)
				return;
			if (!['mimikyu', 'mimikyutotem'].includes(target.species.id) || target.transformed) {
				return;
			}
			var hitSub = target.volatiles['substitute'] && !move.flags['authentic'] && !(move.infiltrates && this.gen >= 6);
			if (hitSub)
				return;
			if (!target.runImmunity(move.type))
				return;
			return False;
		}
	""" 
	pass

def onEffectiveness(**bvalues):
	"""function (typeMod, target, type, move) {
			if (!target || move.category === 'Status')
				return;
			if (!['mimikyu', 'mimikyutotem'].includes(target.species.id) || target.transformed) {
				return;
			}
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
			if (['mimikyu', 'mimikyutotem'].includes(pokemon.species.id) && this.effectState.busted) {
				var speciesid = pokemon.species.id === 'mimikyutotem' ? 'Mimikyu-Busted-Totem' : 'Mimikyu-Busted';
				pokemon.formeChange(speciesid, this.effect, True);
				this.damage(pokemon.baseMaxhp / 8, pokemon, pokemon, this.dex.species.get(speciesid));
			}
		}
	""" 
	pass
