def onSideStart(**bvalues):
	"""function (target, source) {
				this.add('-singleturn', source, 'Crafty Shield');
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				if (['self', 'all'].includes(move.target) || move.category !== 'Status')
					return;
				this.add('-activate', target, 'move: Crafty Shield');
				return this.NOT_FAIL;
			}
	""" 
	pass

def onTry(**bvalues):
	"""function () {
			return !!this.queue.willAct();
		}
	""" 
	pass
