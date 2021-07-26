def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (this.effectData.target.activeTurns) return;

			if (target === source || move.hasBounced || !move.flags['reflectable']) {
				return;
			}
			let newMove = this.getActiveMove(move.id);
			newMove.hasBounced = true;
			this.useMove(newMove, target, source);
			return null;
		}
	""" 
	pass

def onAllyTryHitSide(**bvalues):
	"""function (target, source, move) {
			if (this.effectData.target.activeTurns) return;

			if (target.side === source.side || move.hasBounced || !move.flags['reflectable']) {
				return;
			}
			let newMove = this.getActiveMove(move.id);
			newMove.hasBounced = true;
			this.useMove(newMove, this.effectData.target, source);
			return null;
		}
	""" 
	pass
