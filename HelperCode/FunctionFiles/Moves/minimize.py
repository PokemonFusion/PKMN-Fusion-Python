def onAccuracy (accuracy, target, source, move):
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

def onSourceModifyDamage (damage, source, target, move):
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