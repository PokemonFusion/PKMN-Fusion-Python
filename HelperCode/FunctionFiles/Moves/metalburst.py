def damageCallback (pokemon):
	"""function (pokemon) {
			var lastDamagedBy = pokemon.getLastDamagedBy(true);
			if (lastDamagedBy !== undefined) {
				return (lastDamagedBy.damage * 1.5) || 1;
			}
			return 0;
		}
	""" 
	pass

def onModifyTarget (targetRelayVar, source, target, move):
	"""function (targetRelayVar, source, target, move) {
			var lastDamagedBy = source.getLastDamagedBy(true);
			if (lastDamagedBy) {
				targetRelayVar.target = this.getAtSlot(lastDamagedBy.slot);
			}
		}
	""" 
	pass

def onTryHit (target, source, move):
	"""function (target, source, move) {
			var lastDamagedBy = source.getLastDamagedBy(true);
			if (lastDamagedBy === undefined || !lastDamagedBy.thisTurn)
				return false;
		}
	""" 
	pass