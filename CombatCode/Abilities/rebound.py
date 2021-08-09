def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (this.effectState.target.activeTurns)
				return;
			if (target === source || move.hasBounced || !move.flags['reflectable']) {
				return;
			}
			var newMove = this.dex.getActiveMove(move.id);
			newMove.hasBounced = True;
			this.actions.useMove(newMove, target, source);
			return null;
		}
	""" 
	pass

def onAllyTryHitSide(**bvalues):
	"""function (target, source, move) {
			if (this.effectState.target.activeTurns)
				return;
			if (target.isAlly(source) || move.hasBounced || !move.flags['reflectable']) {
				return;
			}
			var newMove = this.dex.getActiveMove(move.id);
			newMove.hasBounced = True;
			this.actions.useMove(newMove, this.effectState.target, source);
			return null;
		}
	""" 
	pass
