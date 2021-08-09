def onSourceAfterFaint (length, target, source, effect):
	"""function (length, target, source, effect) {
			var _a;
			if (effect && effect.effectType === 'Move') {
				var statName = 'atk';
				var bestStat = 0;
				var s = void 0;
				for (s in source.storedStats) {
					if (source.storedStats[s] > bestStat) {
						statName = s;
						bestStat = source.storedStats[s];
					}
				}
				this.boost((_a = {}, _a[statName] = length, _a), source);
			}
		}
	""" 
	pass