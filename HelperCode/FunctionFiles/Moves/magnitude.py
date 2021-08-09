def onModifyMove (move, pokemon):
	"""function (move, pokemon) {
			var i = this.random(100);
			if (i < 5) {
				move.magnitude = 4;
				move.basePower = 10;
			}
			else if (i < 15) {
				move.magnitude = 5;
				move.basePower = 30;
			}
			else if (i < 35) {
				move.magnitude = 6;
				move.basePower = 50;
			}
			else if (i < 65) {
				move.magnitude = 7;
				move.basePower = 70;
			}
			else if (i < 85) {
				move.magnitude = 8;
				move.basePower = 90;
			}
			else if (i < 95) {
				move.magnitude = 9;
				move.basePower = 110;
			}
			else {
				move.magnitude = 10;
				move.basePower = 150;
			}
		}
	""" 
	pass

def onUseMoveMessage (pokemon, target, move):
	"""function (pokemon, target, move) {
			this.add('-activate', pokemon, 'move: Magnitude', move.magnitude);
		}
	""" 
	pass