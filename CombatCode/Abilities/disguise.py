def onDamage(**bvalues):
	"""function (damage, target, source, effect) {
			if (effect && effect.effectType === 'Move' && ['mimikyu', 'mimikyutotem'].includes(target.template.speciesid) && !target.transformed) {
				this.add('-activate', target, 'ability: Disguise');
				this.effectData.busted = true;
				return 0;
			}
		}
	""" 
	pass

def onEffectiveness(**bvalues):
	"""function (typeMod, target, type, move) {
			if (!this.activeTarget) return;
			let pokemon = this.activeTarget;
			if (!['mimikyu', 'mimikyutotem'].includes(pokemon.template.speciesid) || pokemon.transformed || (pokemon.volatiles['substitute'] && !(move.flags['authentic'] || move.infiltrates))) return;
			if (!pokemon.runImmunity(move.type)) return;
			return 0;
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (['mimikyu', 'mimikyutotem'].includes(pokemon.template.speciesid) && this.effectData.busted) {
				let templateid = pokemon.template.speciesid === 'mimikyutotem' ? 'Mimikyu-Busted-Totem' : 'Mimikyu-Busted';
				pokemon.formeChange(templateid, this.effect, true);
			}
		}
	""" 
	pass
