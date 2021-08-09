def onHit (pokemon):
	"""function (pokemon) {
			var noSleepTalk = [
				'assist', 'beakblast', 'belch', 'bide', 'celebrate', 'chatter', 'copycat', 'dynamaxcannon', 'focuspunch', 'mefirst', 'metronome', 'mimic', 'mirrormove', 'naturepower', 'shelltrap', 'sketch', 'sleeptalk', 'uproar',
			];
			var moves = [];
			for (var _i = 0, _a = pokemon.moveSlots; _i < _a.length; _i++) {
				var moveSlot = _a[_i];
				var moveid = moveSlot.id;
				if (!moveid)
					continue;
				var move = this.dex.moves.get(moveid);
				if (noSleepTalk.includes(moveid) || move.flags['charge'] || (move.isZ && move.basePower !== 1)) {
					continue;
				}
				moves.push(moveid);
			}
			var randomMove = '';
			if (moves.length)
				randomMove = this.sample(moves);
			if (!randomMove) {
				return false;
			}
			this.actions.useMove(randomMove, pokemon);
		}
	""" 
	pass

def onTry (source):
	"""function (source) {
			return source.status === 'slp' || source.hasAbility('comatose');
		}
	""" 
	pass