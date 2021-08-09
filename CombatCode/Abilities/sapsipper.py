def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (target !== source && move.type === 'Grass') {
				if (!this.boost({ atk: 1 })) {
					this.add('-immune', target, '[from] ability: Sap Sipper');
				}
				return null;
			}
		}
	""" 
	pass

def onAllyTryHitSide(**bvalues):
	"""function (target, source, move) {
			if (source === this.effectState.target || !target.isAlly(source))
				return;
			if (move.type === 'Grass') {
				this.boost({ atk: 1 }, this.effectState.target);
			}
		}
	""" 
	pass
