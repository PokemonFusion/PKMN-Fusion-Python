def effect(**bvalues):
	"""function (pokemon) {
				let activate = False;
				/**@type {{[k: string]: number}} */
				let boosts = {};
				for (let i in pokemon.boosts) {
					// @ts-ignore
					if (pokemon.boosts[i] < 0) {
						activate = True;
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
			let activate = False;
			/**@type {{[k: string]: number}} */
			let boosts = {};
			for (let i in pokemon.boosts) {
				// @ts-ignore
				if (pokemon.boosts[i] < 0) {
					activate = True;
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
