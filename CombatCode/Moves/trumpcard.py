def basePowerCallback(**bvalues):
	"""function (source, target, move) {
			var callerMoveId = move.sourceEffect || move.id;
			var moveSlot = callerMoveId === 'instruct' ? source.getMoveData(move.id) : source.getMoveData(callerMoveId);
			if (!moveSlot)
				return 40;
			switch (moveSlot.pp) {
				case 0:
					return 200;
				case 1:
					return 80;
				case 2:
					return 60;
				case 3:
					return 50;
				default:
					return 40;
			}
		}
	""" 
	pass
