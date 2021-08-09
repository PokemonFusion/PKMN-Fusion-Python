def onHit (target, source, move):
	"""function (target, source, move) {
			if (!target.setStatus('slp', source, move))
				return false;
			target.statusState.time = 3;
			target.statusState.startTime = 3;
			this.heal(target.maxhp); // Aesthetic only as the healing happens after you fall asleep in-game
		}
	""" 
	pass

def onTry (source):
	"""function (source) {
			if (source.status === 'slp' || source.hasAbility('comatose'))
				return false;
			if (source.hp === source.maxhp) {
				this.add('-fail', source, 'heal');
				return null;
			}
			if (source.hasAbility(['insomnia', 'vitalspirit'])) {
				this.add('-fail', source, '[from] ability: ' + source.getAbility().name, '[of] ' + source);
				return null;
			}
		}
	""" 
	pass