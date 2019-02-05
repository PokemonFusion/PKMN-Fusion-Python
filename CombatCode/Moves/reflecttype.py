def onHit(datadic : dict):
	"""function (target, source) {
			if (source.template && (source.template.num === 493 || source.template.num === 773)) return false;
			this.add('-start', source, 'typechange', '[from] move: Reflect Type', '[of] ' + target);
			let newBaseTypes = target.getTypes(true).filter(type => type !== '???');
			if (!newBaseTypes.length) {
				if (target.addedType) {
					newBaseTypes = ['Normal'];
				} else {
					return false;
				}
			}
			source.setType(newBaseTypes);
			source.addedType = target.addedType;
			source.knownType = target.side === source.side && target.knownType;
		}
	""" 
	pass
