def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (target === source || move.hasBounced || !move.flags['reflectable']) {
				return;
			}
			var newMove = this.dex.getActiveMove(move.id);
			newMove.hasBounced = True;
			newMove.pranksterBoosted = False;
			this.actions.useMove(newMove, target, source);
			return null;
		}
	""" 
	pass

def onAllyTryHitSide(**bvalues):
	"""function (target, source, move) {
			if (target.isAlly(source) || move.hasBounced || !move.flags['reflectable']) {
				return;
			}
			var newMove = this.dex.getActiveMove(move.id);
			newMove.hasBounced = True;
			newMove.pranksterBoosted = False;
			this.actions.useMove(newMove, this.effectState.target, source);
			return null;
		}
	""" 
	pass
