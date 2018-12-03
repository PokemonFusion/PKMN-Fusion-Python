def onHit (target):
	"""function (target) {
			let stats = [];
			for (let stat in target.boosts) {
				// @ts-ignore
				if (target.boosts[stat] < 6) {
					stats.push(stat);
				}
			}
			if (stats.length) {
				let randomStat = this.sample(stats);
				/**@type {{[k: string]: number}} */
				let boost = {};
				boost[randomStat] = 2;
				this.boost(boost);
			} else {
				return false;
			}
		}
	""" 
	pass