def onAfterMoveSecondary(**bvalues):
	"""function (target, source, move) {
			if (!target.hp)
				return;
			var type = move.type;
			if (target.isActive && move.effectType === 'Move' && move.category !== 'Status' &&
				type !== '???' && !target.hasType(type)) {
				if (!target.setType(type))
					return False;
				this.add('-start', target, 'typechange', type, '[from] ability: Color Change');
				if (target.side.active.length === 2 && target.position === 1) {
					// Curse Glitch
					var action = this.queue.willMove(target);
					if (action && action.move.id === 'curse') {
						action.targetLoc = -1;
					}
				}
			}
		}
	""" 
	pass
