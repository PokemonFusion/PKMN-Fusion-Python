def onModifyType(**bvalues):
	"""function (move) {
				if (move.type === 'Normal') {
					move.type = 'Electric';
					this.debug(move.name + "'s type changed to Electric");
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source, sourceEffect) {
				this.add('-fieldactivate', 'move: Ion Deluge');
				this.hint("Normal-type moves become Electric-type after using " + sourceEffect + ".");
			}
	""" 
	pass
