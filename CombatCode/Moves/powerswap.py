def onHit (target, source):
	"""function (target, source) {
			let targetBoosts = {};
			let sourceBoosts = {};

			for (const stat of ['atk', 'spa']) {
				// @ts-ignore
				targetBoosts[stat] = target.boosts[stat];
				// @ts-ignore
				sourceBoosts[stat] = source.boosts[stat];
			}

			source.setBoost(targetBoosts);
			target.setBoost(sourceBoosts);

			this.add('-swapboost', source, target, 'atk, spa', '[from] move: Power Swap');
		}
	""" 
	pass