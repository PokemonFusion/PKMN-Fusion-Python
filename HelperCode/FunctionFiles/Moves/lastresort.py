def onTry (source):
	"""function (source) {
			if (source.moveSlots.length < 2)
				return false; // Last Resort fails unless the user knows at least 2 moves
			var hasLastResort = false; // User must actually have Last Resort for it to succeed
			for (var _i = 0, _a = source.moveSlots; _i < _a.length; _i++) {
				var moveSlot = _a[_i];
				if (moveSlot.id === 'lastresort') {
					hasLastResort = true;
					continue;
				}
				if (!moveSlot.used)
					return false;
			}
			return hasLastResort;
		}
	""" 
	pass