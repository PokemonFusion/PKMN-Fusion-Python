def onSideStart (target, source):
	"""function (target, source) {
				this.add('-singleturn', source, 'Crafty Shield');
			}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
				if (['self', 'all'].includes(move.target) || move.category !== 'Status')
					return;
				this.add('-activate', target, 'move: Crafty Shield');
				return this.NOT_FAIL;
			}
	""" 
	pass

def onTry ():
	"""function () {
			return !!this.queue.willAct();
		}
	""" 
	pass