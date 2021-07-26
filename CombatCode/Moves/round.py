def basePowerCallback(**bvalues):
	"""function (target, source, move) {
			if (move.sourceEffect === 'round') {
				return move.basePower * 2;
			}
			return move.basePower;
		}
	""" 
	pass

def onTry(**bvalues):
	"""function () {
			for (const action of this.queue) {
				// @ts-ignore
				if (!action.pokemon || !action.move) continue;
				// @ts-ignore
				if (action.move.id === 'round') {
					// @ts-ignore
					this.prioritizeAction(action);
					return;
				}
			}
		}
	""" 
	pass
