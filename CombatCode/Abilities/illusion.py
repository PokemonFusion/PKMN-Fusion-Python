def onBeforeSwitchIn (pokemon):
	"""function (pokemon) {
			pokemon.illusion = null;
			let i;
			for (i = pokemon.side.pokemon.length - 1; i > pokemon.position; i--) {
				if (!pokemon.side.pokemon[i]) continue;
				if (!pokemon.side.pokemon[i].fainted) break;
			}
			if (!pokemon.side.pokemon[i]) return;
			if (pokemon === pokemon.side.pokemon[i]) return;
			pokemon.illusion = pokemon.side.pokemon[i];
		}
	""" 
	pass

def onAfterDamage (damage, target, source, effect):
	"""function (damage, target, source, effect) {
			if (target.illusion && effect && effect.effectType === 'Move' && effect.id !== 'confused') {
				this.singleEvent('End', this.getAbility('Illusion'), target.abilityData, target, source, effect);
			}
		}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
			if (pokemon.illusion) {
				this.debug('illusion cleared');
				pokemon.illusion = null;
				let details = pokemon.template.species + (pokemon.level === 100 ? '' : ', L' + pokemon.level) + (pokemon.gender === '' ? '' : ', ' + pokemon.gender) + (pokemon.set.shiny ? ', shiny' : '');
				this.add('replace', pokemon, details);
				this.add('-end', pokemon, 'Illusion');
			}
		}
	""" 
	pass

def onFaint (pokemon):
	"""function (pokemon) {
			pokemon.illusion = null;
		}
	""" 
	pass