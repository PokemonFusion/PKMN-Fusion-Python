def effect(**bvalues):
	"""function (pokemon) {
				var activate = false;
				var boosts = {};
				var i;
				for (i in pokemon.boosts) {
					if (pokemon.boosts[i] < 0) {
						activate = true;
						boosts[i] = 0;
					}
				}
				if (activate) {
					pokemon.setBoost(boosts);
					this.add('-clearnegativeboost', pokemon, '[silent]');
				}
			}
	""" 
	pass

def onUpdate(**bvalues):
	"""function (pokemon) {
			var activate = false;
			var boosts = {};
			var i;
			for (i in pokemon.boosts) {
				if (pokemon.boosts[i] < 0) {
					activate = true;
					boosts[i] = 0;
				}
			}
			if (activate && pokemon.useItem()) {
				pokemon.setBoost(boosts);
				this.add('-clearnegativeboost', pokemon, '[silent]');
			}
		}
	""" 
	pass
