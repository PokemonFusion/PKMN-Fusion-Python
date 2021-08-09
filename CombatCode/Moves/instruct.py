def onHit(**bvalues):
	"""function (target, source) {
			if (!target.lastMove || target.volatiles['dynamax'])
				return false;
			var lastMove = target.lastMove;
			var moveIndex = target.moves.indexOf(lastMove.id);
			var noInstruct = [
				'assist', 'beakblast', 'belch', 'bide', 'celebrate', 'copycat', 'dynamaxcannon', 'focuspunch', 'iceball', 'instruct', 'kingsshield', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'obstruct', 'outrage', 'petaldance', 'rollout', 'shelltrap', 'sketch', 'sleeptalk', 'struggle', 'thrash', 'transform', 'uproar',
			];
			if (noInstruct.includes(lastMove.id) || lastMove.isZ || lastMove.isMax ||
				lastMove.flags['charge'] || lastMove.flags['recharge'] ||
				target.volatiles['beakblast'] || target.volatiles['focuspunch'] || target.volatiles['shelltrap'] ||
				(target.moveSlots[moveIndex] && target.moveSlots[moveIndex].pp <= 0)) {
				return false;
			}
			this.add('-singleturn', target, 'move: Instruct', '[of] ' + source);
			this.actions.runMove(target.lastMove.id, target, target.lastMoveTargetLoc);
		}
	""" 
	pass
