def onHit(**bvalues):
	"""function (target, source) {
			if (!target.lastMove) return false;
			let lastMove = target.lastMove;
			let moveIndex = target.moves.indexOf(lastMove.id);
			let noInstruct = [
				'assist', 'beakblast', 'bide', 'copycat', 'focuspunch', 'iceball', 'instruct', 'kingsshield', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'outrage', 'petaldance', 'rollout', 'shelltrap', 'sketch', 'sleeptalk', 'thrash', 'transform',
			];
			if (noInstruct.includes(lastMove.id) || lastMove.isZ || lastMove.flags['charge'] || lastMove.flags['recharge'] || target.volatiles['beakblast'] || target.volatiles['focuspunch'] || target.volatiles['shelltrap'] || (target.moveSlots[moveIndex] && target.moveSlots[moveIndex].pp <= 0)) {
				return false;
			}
			this.add('-singleturn', target, 'move: Instruct', '[of] ' + source);
			this.runMove(target.lastMove.id, target, target.lastMoveTargetLoc);
		}
	""" 
	pass
