def effect(**bvalues):
	"""function (pokemon) {
				var conditions = ['attract', 'taunt', 'encore', 'torment', 'disable', 'healblock'];
				for (var _i = 0, conditions_1 = conditions; _i < conditions_1.length; _i++) {
					var firstCondition = conditions_1[_i];
					if (pokemon.volatiles[firstCondition]) {
						for (var _a = 0, conditions_2 = conditions; _a < conditions_2.length; _a++) {
							var secondCondition = conditions_2[_a];
							pokemon.removeVolatile(secondCondition);
							if (firstCondition === 'attract' && secondCondition === 'attract') {
								this.add('-end', pokemon, 'move: Attract', '[from] item: Mental Herb');
							}
						}
						return;
					}
				}
			}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			var conditions = ['attract', 'taunt', 'encore', 'torment', 'disable', 'healblock'];
			for (var _i = 0, conditions_3 = conditions; _i < conditions_3.length; _i++) {
				var firstCondition = conditions_3[_i];
				if (pokemon.volatiles[firstCondition]) {
					if (!pokemon.useItem())
						return;
					for (var _a = 0, conditions_4 = conditions; _a < conditions_4.length; _a++) {
						var secondCondition = conditions_4[_a];
						pokemon.removeVolatile(secondCondition);
						if (firstCondition === 'attract' && secondCondition === 'attract') {
							this.add('-end', pokemon, 'move: Attract', '[from] item: Mental Herb');
						}
					}
					return;
				}
			}
		}
	""" 
	pass
