def onTryHeal(**bvalues):
	"""function (damage, target, source, effect) {
			if (!effect)
				return;
			if (effect.id === 'berryjuice' || effect.id === 'leftovers') {
				this.add('-activate', target, 'ability: Ripen');
			}
			if (effect.isBerry)
				return this.chainModify(2);
		}
	""" 
	pass

def onBoost(**bvalues):
	"""function (boost, target, source, effect) {
			if (effect && effect.isBerry) {
				var b = void 0;
				for (b in boost) {
					boost[b] *= 2;
				}
			}
		}
	""" 
	pass

def onSourceModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
			if (target.abilityState.berryWeaken) {
				target.abilityState.berryWeaken = False;
				return this.chainModify(0.5);
			}
		}
	""" 
	pass

def onTryEatItem(**bvalues):
	"""function (item, pokemon) {
			this.add('-activate', pokemon, 'ability: Ripen');
		}
	""" 
	pass

def onEatItem(**bvalues):
	"""function (item, pokemon) {
			var weakenBerries = [
				'Babiri Berry', 'Charti Berry', 'Chilan Berry', 'Chople Berry', 'Coba Berry', 'Colbur Berry', 'Haban Berry', 'Kasib Berry', 'Kebia Berry', 'Occa Berry', 'Passho Berry', 'Payapa Berry', 'Rindo Berry', 'Roseli Berry', 'Shuca Berry', 'Tanga Berry', 'Wacan Berry', 'Yache Berry',
			];
			// Record if the pokemon ate a berry to resist the attack
			pokemon.abilityState.berryWeaken = weakenBerries.includes(item.name);
		}
	""" 
	pass
