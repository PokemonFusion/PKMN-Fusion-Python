def onHit(datadic : dict):
	"""function (target, source) {
			if (!target.lastMove) {
				return false;
			}
			let possibleTypes = [];
			let attackType = target.lastMove.type;
			for (let type in this.data.TypeChart) {
				if (source.hasType(type)) continue;
				let typeCheck = this.data.TypeChart[type].damageTaken[attackType];
				if (typeCheck === 2 || typeCheck === 3) {
					possibleTypes.push(type);
				}
			}
			if (!possibleTypes.length) {
				return false;
			}
			let randomType = this.sample(possibleTypes);

			if (!source.setType(randomType)) return false;
			this.add('-start', source, 'typechange', randomType);
		}
	""" 
	pass
