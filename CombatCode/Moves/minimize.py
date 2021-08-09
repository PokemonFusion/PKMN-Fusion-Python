def onAccuracy(**bvalues):
	"""function (accuracy, target, source, move) {
				var boostedMoves = [
					'stomp', 'steamroller', 'bodyslam', 'flyingpress', 'dragonrush', 'heatcrash', 'heavyslam', 'maliciousmoonsault',
				];
				if (boostedMoves.includes(move.id)) {
					return true;
				}
				return accuracy;
			}
	""" 
	pass

def onSourceModifyDamage(**bvalues):
	"""function (damage, source, target, move) {
				var boostedMoves = [
					'stomp', 'steamroller', 'bodyslam', 'flyingpress', 'dragonrush', 'heatcrash', 'heavyslam', 'maliciousmoonsault',
				];
				if (boostedMoves.includes(move.id)) {
					return this.chainModify(2);
				}
			}
	""" 
	pass
