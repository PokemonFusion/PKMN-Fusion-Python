def onResidual (pokemon):
	"""function (pokemon) {
			var stats = [];
			var boost = {};
			var statPlus;
			for (statPlus in pokemon.boosts) {
				if (statPlus === 'accuracy' || statPlus === 'evasion')
					continue;
				if (pokemon.boosts[statPlus] < 6) {
					stats.push(statPlus);
				}
			}
			var randomStat = stats.length ? this.sample(stats) : undefined;
			if (randomStat)
				boost[randomStat] = 2;
			stats = [];
			var statMinus;
			for (statMinus in pokemon.boosts) {
				if (statMinus === 'accuracy' || statMinus === 'evasion')
					continue;
				if (pokemon.boosts[statMinus] > -6 && statMinus !== randomStat) {
					stats.push(statMinus);
				}
			}
			randomStat = stats.length ? this.sample(stats) : undefined;
			if (randomStat)
				boost[randomStat] = -1;
			this.boost(boost);
		}
	""" 
	pass