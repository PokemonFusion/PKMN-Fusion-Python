def onSourceFaint (target, source, effect):
	"""function (target, source, effect) {
			if (effect && effect.effectType === 'Move' && source.template.speciesid === 'greninja' && source.hp && !source.transformed && source.side.foe.pokemonLeft) {
				this.add('-activate', source, 'ability: Battle Bond');
				source.formeChange('Greninja-Ash', this.effect, true);
			}
		}
	""" 
	pass

def onModifyMove (move, attacker):
	"""function (move, attacker) {
			if (move.id === 'watershuriken' && attacker.template.species === 'Greninja-Ash') {
				move.multihit = 3;
			}
		}
	""" 
	pass