def onBoost(**bvalues):
	"""function (boost, target, source, effect) {
			// Don't bounce self stat changes, or boosts that have already bounced
			if (target === source || !boost || effect.id === 'mirrorarmor')
				return;
			var b;
			for (b in boost) {
				if (boost[b] < 0) {
					if (target.boosts[b] === -6)
						continue;
					var negativeBoost = {};
					negativeBoost[b] = boost[b];
					delete boost[b];
					this.add('-ability', target, 'Mirror Armor');
					this.boost(negativeBoost, source, target, null, True);
				}
			}
		}
	""" 
	pass
