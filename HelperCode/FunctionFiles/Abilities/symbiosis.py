def onAllyAfterUseItem (item, pokemon):
	"""function (item, pokemon) {
			if (pokemon.switchFlag)
				return;
			var source = this.effectState.target;
			var myItem = source.takeItem();
			if (!myItem)
				return;
			if (!this.singleEvent('TakeItem', myItem, source.itemState, pokemon, source, this.effect, myItem) ||
				!pokemon.setItem(myItem)) {
				source.item = myItem.id;
				return;
			}
			this.add('-activate', source, 'ability: Symbiosis', myItem, '[of] ' + pokemon);
		}
	""" 
	pass