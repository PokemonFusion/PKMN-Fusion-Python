def onSourceAfterFaint(**bvalues):
	"""function (length, target, source, effect) {
			if ((effect === null || effect === void 0 ? void 0 : effect.effectType) !== 'Move') {
				return;
			}
			if (source.species.id === 'greninja' && source.hp && !source.transformed && source.side.foePokemonLeft()) {
				this.add('-activate', source, 'ability: Battle Bond');
				source.formeChange('Greninja-Ash', this.effect, True);
			}
		}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move, attacker) {
			if (move.id === 'watershuriken' && attacker.species.name === 'Greninja-Ash') {
				move.multihit = 3;
			}
		}
	""" 
	pass
