def onAllyAfterUseItem(datadic : dict):
	"""function (item, pokemon) {
			let source = this.effectData.target;
			let myItem = source.takeItem();
			if (!myItem) return;
			// @ts-ignore
			if (!this.singleEvent('TakeItem', myItem, source.itemData, pokemon, source, this.effectData, myItem) || !pokemon.setItem(myItem)) {
				source.item = myItem.id;
				return;
			}
			this.add('-activate', source, 'ability: Symbiosis', myItem, '[of] ' + pokemon);
		}
	""" 
	pass
