def onStart(**bvalues):
	"""function (target, source, effect) {
				this.add('-singleturn', target, 'move: Magic Coat');
				if (effect && effect.effectType === 'Move') {
					this.effectData.pranksterBoosted = effect.pranksterBoosted;
				}
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				if (target === source || move.hasBounced || !move.flags['reflectable']) {
					return;
				}
				let newMove = this.getActiveMove(move.id);
				newMove.hasBounced = true;
				newMove.pranksterBoosted = this.effectData.pranksterBoosted;
				this.useMove(newMove, target, source);
				return null;
			}
	""" 
	pass

def onAllyTryHitSide(**bvalues):
	"""function (target, source, move) {
				if (target.side === source.side || move.hasBounced || !move.flags['reflectable']) {
					return;
				}
				let newMove = this.getActiveMove(move.id);
				newMove.hasBounced = true;
				newMove.pranksterBoosted = false;
				this.useMove(newMove, this.effectData.target, source);
				return null;
			}
	""" 
	pass
