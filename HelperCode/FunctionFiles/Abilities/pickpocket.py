def onAfterMoveSecondary (target, source, move):
	"""function (target, source, move) {
			if (source && source !== target && (move === null || move === void 0 ? void 0 : move.flags['contact'])) {
				if (target.item || target.switchFlag || target.forceSwitchFlag || source.switchFlag === True) {
					return;
				}
				var yourItem = source.takeItem(target);
				if (!yourItem) {
					return;
				}
				if (!target.setItem(yourItem)) {
					source.item = yourItem.id;
					return;
				}
				this.add('-enditem', source, yourItem, '[silent]', '[from] ability: Pickpocket', '[of] ' + source);
				this.add('-item', target, yourItem, '[from] ability: Pickpocket', '[of] ' + source);
			}
		}
	""" 
	pass