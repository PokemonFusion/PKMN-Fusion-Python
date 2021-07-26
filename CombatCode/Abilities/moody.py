def onResidual(**bvalues):
	"""function (pokemon) {
			let stats = [];
			let boost = {};
			for (let statPlus in pokemon.boosts) {
				// @ts-ignore
				if (pokemon.boosts[statPlus] < 6) {
					stats.push(statPlus);
				}
			}
			let randomStat = stats.length ? this.sample(stats) : "";
			// @ts-ignore
			if (randomStat) boost[randomStat] = 2;

			stats = [];
			for (let statMinus in pokemon.boosts) {
				// @ts-ignore
				if (pokemon.boosts[statMinus] > -6 && statMinus !== randomStat) {
					stats.push(statMinus);
				}
			}
			randomStat = stats.length ? this.sample(stats) : "";
			// @ts-ignore
			if (randomStat) boost[randomStat] = -1;

			this.boost(boost);
		}
	""" 
	pass
