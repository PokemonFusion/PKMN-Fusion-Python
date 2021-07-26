def onTryHit(**bvalues):
	"""function (pokemon) {
			if (pokemon.status !== 'slp' && !pokemon.hasAbility('comatose')) return false;
		}
	""" 
	pass

def onHit(**bvalues):
	"""function (pokemon) {
			let moves = [];
			for (const moveSlot of pokemon.moveSlots) {
				const move = moveSlot.id;
				const noSleepTalk = [
					'assist', 'beakblast', 'belch', 'bide', 'chatter', 'copycat', 'focuspunch', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'shelltrap', 'sketch', 'sleeptalk', 'uproar',
				];
				if (move && !(noSleepTalk.includes(move) || this.getMove(move).flags['charge'] || (this.getMove(move).isZ && this.getMove(move).basePower !== 1))) {
					moves.push(move);
				}
			}
			let randomMove = '';
			if (moves.length) randomMove = this.sample(moves);
			if (!randomMove) {
				return false;
			}
			this.useMove(randomMove, pokemon);
		}
	""" 
	pass
