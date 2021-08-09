def onEat(**bvalues):
	"""function (pokemon) {
			var stats = [];
			var stat;
			for (stat in pokemon.boosts) {
				if (stat !== 'accuracy' && stat !== 'evasion' && pokemon.boosts[stat] < 6) {
					stats.push(stat);
				}
			}
			if (stats.length) {
				var randomStat = this.sample(stats);
				var boost = {};
				boost[randomStat] = 2;
				this.boost(boost);
			}
		}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			if (pokemon.hp <= pokemon.maxhp / 4 || (pokemon.hp <= pokemon.maxhp / 2 && pokemon.hasAbility('gluttony'))) {
				pokemon.eatItem();
			}
		}
	""" 
	pass
