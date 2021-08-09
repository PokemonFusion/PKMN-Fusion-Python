def onBasePower(**bvalues):
	"""function (basePower) {
				return this.chainModify(1.5);
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, pokemon) {
			var action = this.queue.willMove(target);
			if (!action)
				return false;
			var noMeFirst = [
				'beakblast', 'chatter', 'counter', 'covet', 'focuspunch', 'mefirst', 'metalburst', 'mirrorcoat', 'shelltrap', 'struggle', 'thief',
			];
			var move = this.dex.getActiveMove(action.move.id);
			if (action.zmove || move.isZ || move.isMax)
				return false;
			if (target.volatiles['mustrecharge'])
				return false;
			if (move.category === 'Status' || noMeFirst.includes(move.id))
				return false;
			pokemon.addVolatile('mefirst');
			this.actions.useMove(move, pokemon, target);
			return null;
		}
	""" 
	pass
