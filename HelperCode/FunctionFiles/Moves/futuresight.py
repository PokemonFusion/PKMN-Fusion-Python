def onTry (source, target):
	"""function (source, target) {
			if (!target.side.addSlotCondition(target, 'futuremove'))
				return false;
			Object.assign(target.side.slotConditions[target.position]['futuremove'], {
				duration: 3,
				move: 'futuresight',
				source: source,
				moveData: {
					id: 'futuresight',
					name: "Future Sight",
					accuracy: 100,
					basePower: 120,
					category: "Special",
					priority: 0,
					flags: {},
					ignoreImmunity: false,
					effectType: 'Move',
					isFutureMove: true,
					type: 'Psychic',
				},
			});
			this.add('-start', source, 'move: Future Sight');
			return this.NOT_FAIL;
		}
	""" 
	pass