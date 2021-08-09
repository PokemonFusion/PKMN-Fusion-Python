def onPreStart(**bvalues):
	"""function (pokemon) {
			this.add('-ability', pokemon, 'Neutralizing Gas');
			pokemon.abilityState.ending = False;
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var target = _a[_i];
				if (target.illusion) {
					this.singleEvent('End', this.dex.abilities.get('Illusion'), target.abilityState, target, pokemon, 'neutralizinggas');
				}
				if (target.volatiles['slowstart']) {
					delete target.volatiles['slowstart'];
					this.add('-end', target, 'Slow Start', '[silent]');
				}
			}
		}
	""" 
	pass

def onEnd(**bvalues):
	"""function (source) {
			for (var _i = 0, _a = this.getAllActive(); _i < _a.length; _i++) {
				var pokemon = _a[_i];
				if (pokemon !== source && pokemon.hasAbility('Neutralizing Gas')) {
					return;
				}
			}
			this.add('-end', source, 'ability: Neutralizing Gas');
			// FIXME this happens before the pokemon switches out, should be the opposite order.
			// Not an easy fix since we cant use a supported event. Would need some kind of special event that
			// gathers events to run after the switch and then runs them when the ability is no longer accessible.
			// (If you're tackling this, do note extreme weathers have the same issue)
			// Mark this pokemon's ability as ending so Pokemon#ignoringAbility skips it
			if (source.abilityState.ending)
				return;
			source.abilityState.ending = True;
			var sortedActive = this.getAllActive();
			this.speedSort(sortedActive);
			for (var _b = 0, sortedActive_1 = sortedActive; _b < sortedActive_1.length; _b++) {
				var pokemon = sortedActive_1[_b];
				if (pokemon !== source) {
					// Will be suppressed by Pokemon#ignoringAbility if needed
					this.singleEvent('Start', pokemon.getAbility(), pokemon.abilityState, pokemon);
				}
			}
		}
	""" 
	pass
