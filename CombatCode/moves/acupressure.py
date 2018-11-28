import random
def onHit(target):
    #  function (target) {
	# 		let stats = [];
	# 		for (let stat in target.boosts) {
	# 			// @ts-ignore
	# 			if (target.boosts[stat] < 6) {
	# 				stats.push(stat);
	# 			}
	# 		}
	# 		if (stats.length) {
	# 			let randomStat = this.sample(stats);
	# 			/**@type {{["k": string]: number}} */
	# 			let boost = {};
	# 			boost[randomStat] = 2;
	# 			this.boost(boost);
	# 		} else {
	# 			return False;
	# 		}
	# 	}
    stats = []
    for stat in target.boosts:
        if target.boosts[stat] < 6:
            stats.append(stat)
        if len(stats) != 0:
            randomStat = random.sample(stats, 1)
            boost = {}
            boost[randomStat] = 2
            #TODO: call the boost function
            

