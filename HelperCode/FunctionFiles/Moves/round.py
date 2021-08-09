def basePowerCallback (target, source, move):
	"""function (target, source, move) {
			if (move.sourceEffect === 'round') {
				return move.basePower * 2;
			}
			return move.basePower;
		}
	""" 
	pass

def onTry (source, target, move):
	"""function (source, target, move) {
			for (var _i = 0, _a = this.queue.list; _i < _a.length; _i++) {
				var action = _a[_i];
				if (!action.pokemon || !action.move || action.maxMove || action.zmove)
					continue;
				if (action.move.id === 'round') {
					this.queue.prioritizeAction(action, move);
					return;
				}
			}
		}
	""" 
	pass