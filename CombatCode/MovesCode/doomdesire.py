def onTry (source, target):
	"""function (source, target) {
			target.side.addSideCondition('futuremove');
			if (target.side.sideConditions['futuremove'].positions[target.position]) {
				return false;
			}
			target.side.sideConditions['futuremove'].positions[target.position] = {
				duration: 3,
				move: 'doomdesire',
				source: source,
				moveData: {
					id: 'doomdesire',
					name: "Doom Desire",
					accuracy: 100,
					basePower: 140,
					category: "Special",
					priority: 0,
					flags: {},
					effectType: 'Move',
					isFutureMove: true,
					type: 'Steel',
				},
			};
			this.add('-start', source, 'Doom Desire');
			return null;
		}
	""" 
	pass