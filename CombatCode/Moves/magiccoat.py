def onAllyTryHitSide(**bvalues):
	"""function (target, source, move) {
				if (target.isAlly(source) || move.hasBounced || !move.flags['reflectable']) {
					return;
				}
				var newMove = this.dex.getActiveMove(move.id);
				newMove.hasBounced = true;
				newMove.pranksterBoosted = false;
				this.actions.useMove(newMove, this.effectState.target, source);
				return null;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source, effect) {
				this.add('-singleturn', target, 'move: Magic Coat');
				if ((effect === null || effect === void 0 ? void 0 : effect.effectType) === 'Move') {
					this.effectState.pranksterBoosted = effect.pranksterBoosted;
				}
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
				if (target === source || move.hasBounced || !move.flags['reflectable']) {
					return;
				}
				var newMove = this.dex.getActiveMove(move.id);
				newMove.hasBounced = true;
				newMove.pranksterBoosted = this.effectState.pranksterBoosted;
				this.actions.useMove(newMove, target, source);
				return null;
			}
	""" 
	pass
