def onModifyMove(**bvalues):
	"""function (move) {
			if (move.category !== "Status") {
				if (!move.secondaries)
					move.secondaries = [];
				for (var _i = 0, _a = move.secondaries; _i < _a.length; _i++) {
					var secondary = _a[_i];
					if (secondary.volatileStatus === 'flinch')
						return;
				}
				move.secondaries.push({
					chance: 10,
					volatileStatus: 'flinch',
				});
			}
		}
	""" 
	pass
