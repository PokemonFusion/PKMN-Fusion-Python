def onStart(**bvalues):
	"""function (target) {
				this.add('-fieldactivate', 'move: Ion Deluge');
			}
	""" 
	pass

def onModifyMove(**bvalues):
	"""function (move) {
				if (move.type === 'Normal') {
					move.type = 'Electric';
					this.debug(move.name + "'s type changed to Electric");
				}
			}
	""" 
	pass
