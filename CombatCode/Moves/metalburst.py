def damageCallback(**bvalues):
	"""function (pokemon) {
			var lastDamagedBy = pokemon.getLastDamagedBy(true);
			if (lastDamagedBy !== undefined) {
				return (lastDamagedBy.damage * 1.5) || 1;
			}
			return 0;
		}
	""" 
	pass

def onModifyTarget(**bvalues):
	"""function (targetRelayVar, source, target, move) {
			var lastDamagedBy = source.getLastDamagedBy(true);
			if (lastDamagedBy) {
				targetRelayVar.target = this.getAtSlot(lastDamagedBy.slot);
			}
		}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (target, source, move) {
			var lastDamagedBy = source.getLastDamagedBy(true);
			if (lastDamagedBy === undefined || !lastDamagedBy.thisTurn)
				return false;
		}
	""" 
	pass
