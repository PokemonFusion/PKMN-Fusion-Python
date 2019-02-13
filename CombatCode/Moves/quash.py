def onHit(datadic : dict):
	"""function (target) {
			if (target.side.active.length < 2) return false; // fails in singles
			let action = this.willMove(target);
			if (action) {
				action.priority = -7.1;
				this.cancelMove(target);
				for (let i = this.queue.length - 1; i >= 0; i--) {
					if (this.queue[i].choice === 'residual') {
						this.queue.splice(i, 0, action);
						break;
					}
				}
				this.add('-activate', target, 'move: Quash');
			} else {
				return false;
			}
		}
	""" 
	pass
