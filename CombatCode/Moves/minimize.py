def onSourceModifyDamage (damage, source, target, move):
	"""function (damage, source, target, move) {
				if (['stomp', 'steamroller', 'bodyslam', 'flyingpress', 'dragonrush', 'heatcrash', 'heavyslam', 'maliciousmoonsault'].includes(move.id)) {
					return this.chainModify(2);
				}
			}
	""" 
	pass

def onAccuracy (accuracy, target, source, move):
	"""function (accuracy, target, source, move) {
				if (['stomp', 'steamroller', 'bodyslam', 'flyingpress', 'dragonrush', 'heatcrash', 'heavyslam', 'maliciousmoonsault'].includes(move.id)) {
					return true;
				}
				return accuracy;
			}
	""" 
	pass