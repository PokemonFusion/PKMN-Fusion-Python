def onHit (target, source):
	"""function (target, source) {
			if (!target.lastMoveUsed) {
				return false;
			}
			var possibleTypes = [];
			var attackType = target.lastMoveUsed.type;
			for (var _i = 0, _a = this.dex.types.names(); _i < _a.length; _i++) {
				var type = _a[_i];
				if (source.hasType(type))
					continue;
				var typeCheck = this.dex.types.get(type).damageTaken[attackType];
				if (typeCheck === 2 || typeCheck === 3) {
					possibleTypes.push(type);
				}
			}
			if (!possibleTypes.length) {
				return false;
			}
			var randomType = this.sample(possibleTypes);
			if (!source.setType(randomType))
				return false;
			this.add('-start', source, 'typechange', randomType);
		}
	""" 
	pass