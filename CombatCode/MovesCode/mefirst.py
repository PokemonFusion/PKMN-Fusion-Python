def onTryHit (target, pokemon):
	"""function (target, pokemon) {
			let action = this.willMove(target);
			if (action) {
				let noMeFirst = [
					'chatter', 'counter', 'covet', 'focuspunch', 'mefirst', 'metalburst', 'mirrorcoat', 'struggle', 'thief',
				];
				let move = this.getActiveMove(action.move.id);
				if (move.category !== 'Status' && !noMeFirst.includes(move.id)) {
					pokemon.addVolatile('mefirst');
					this.useMove(move, pokemon, target);
					return null;
				}
			}
			return false;
		}
	""" 
	pass

def onBasePower (basePower):
	"""function (basePower) {
				return this.chainModify(1.5);
			}
	""" 
	pass