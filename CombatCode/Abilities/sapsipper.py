def onTryHit(datadic : dict):
	"""function (target, source, move) {
			if (target !== source && move.type === 'Grass') {
				if (!this.boost({atk: 1})) {
					this.add('-immune', target, '[from] ability: Sap Sipper');
				}
				return null;
			}
		}
	""" 
	pass

def onAllyTryHitSide(datadic : dict):
	"""function (target, source, move) {
			if (target === this.effectData.target || target.side !== source.side) return;
			if (move.type === 'Grass') {
				this.boost({atk: 1}, this.effectData.target);
			}
		}
	""" 
	pass
