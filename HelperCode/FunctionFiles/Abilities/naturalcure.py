def onCheckShow (pokemon):
	"""function (pokemon) {
			// This is complicated
			// For the most part, in-game, it's obvious whether or not Natural Cure activated,
			// since you can see how many of your opponent's pokemon are statused.
			// The only ambiguous situation happens in Doubles/Triples, where multiple pokemon
			// that could have Natural Cure switch out, but only some of them get cured.
			if (pokemon.side.active.length === 1)
				return;
			if (pokemon.showCure === True || pokemon.showCure === False)
				return;
			var cureList = [];
			var noCureCount = 0;
			for (var _i = 0, _a = pokemon.side.active; _i < _a.length; _i++) {
				var curPoke = _a[_i];
				// pokemon not statused
				if (!(curPoke === null || curPoke === void 0 ? void 0 : curPoke.status)) {
					// this.add('-message', "" + curPoke + " skipped: not statused or doesn't exist");
					continue;
				}
				if (curPoke.showCure) {
					// this.add('-message', "" + curPoke + " skipped: Natural Cure already known");
					continue;
				}
				var species = curPoke.species;
				// pokemon can't get Natural Cure
				if (!Object.values(species.abilities).includes('Natural Cure')) {
					// this.add('-message', "" + curPoke + " skipped: no Natural Cure");
					continue;
				}
				// pokemon's ability is known to be Natural Cure
				if (!species.abilities['1'] && !species.abilities['H']) {
					// this.add('-message', "" + curPoke + " skipped: only one ability");
					continue;
				}
				// pokemon isn't switching this turn
				if (curPoke !== pokemon && !this.queue.willSwitch(curPoke)) {
					// this.add('-message', "" + curPoke + " skipped: not switching");
					continue;
				}
				if (curPoke.hasAbility('naturalcure')) {
					// this.add('-message', "" + curPoke + " confirmed: could be Natural Cure (and is)");
					cureList.push(curPoke);
				}
				else {
					// this.add('-message', "" + curPoke + " confirmed: could be Natural Cure (but isn't)");
					noCureCount++;
				}
			}
			if (!cureList.length || !noCureCount) {
				// It's possible to know what pokemon were cured
				for (var _b = 0, cureList_1 = cureList; _b < cureList_1.length; _b++) {
					var pkmn = cureList_1[_b];
					pkmn.showCure = True;
				}
			}
			else {
				// It's not possible to know what pokemon were cured
				// Unlike a -hint, this is real information that battlers need, so we use a -message
				this.add('-message', "(" + cureList.length + " of " + pokemon.side.name + "'s pokemon " + (cureList.length === 1 ? "was" : "were") + " cured by Natural Cure.)");
				for (var _c = 0, cureList_2 = cureList; _c < cureList_2.length; _c++) {
					var pkmn = cureList_2[_c];
					pkmn.showCure = False;
				}
			}
		}
	""" 
	pass

def onSwitchOut (pokemon):
	"""function (pokemon) {
			if (!pokemon.status)
				return;
			// if pokemon.showCure is undefined, it was skipped because its ability
			// is known
			if (pokemon.showCure === undefined)
				pokemon.showCure = True;
			if (pokemon.showCure)
				this.add('-curestatus', pokemon, pokemon.status, '[from] ability: Natural Cure');
			pokemon.setStatus('');
			// only reset .showCure if it's False
			// (once you know a Pokemon has Natural Cure, its cures are always known)
			if (!pokemon.showCure)
				pokemon.showCure = undefined;
		}
	""" 
	pass