def onHit(**bvalues):
	"""function (source) {
				if (this.random(2) === 0)
					return;
				for (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {
					var pokemon = _a[_i];
					if (pokemon.item)
						continue;
					if (pokemon.lastItem && this.dex.items.get(pokemon.lastItem).isBerry) {
						var item = pokemon.lastItem;
						pokemon.lastItem = '';
						this.add('-item', pokemon, this.dex.items.get(item), '[from] move: G-Max Replenish');
						pokemon.setItem(item);
					}
				}
			}
	""" 
	pass
