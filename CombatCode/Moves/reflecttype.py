def onHit(**bvalues):
	"""function (target, source) {
			if (source.species && (source.species.num === 493 || source.species.num === 773))
				return false;
			var newBaseTypes = target.getTypes(true).filter(function (type) { return type !== '???'; });
			if (!newBaseTypes.length) {
				if (target.addedType) {
					newBaseTypes = ['Normal'];
				}
				else {
					return false;
				}
			}
			this.add('-start', source, 'typechange', '[from] move: Reflect Type', '[of] ' + target);
			source.setType(newBaseTypes);
			source.addedType = target.addedType;
			source.knownType = target.isAlly(source) && target.knownType;
		}
	""" 
	pass
