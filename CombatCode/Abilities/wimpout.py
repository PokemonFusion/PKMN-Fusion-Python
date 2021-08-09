def onEmergencyExit(**bvalues):
	"""function (target) {
			if (!this.canSwitch(target.side) || target.forceSwitchFlag || target.switchFlag)
				return;
			for (var _i = 0, _a = this.sides; _i < _a.length; _i++) {
				var side = _a[_i];
				for (var _b = 0, _c = side.active; _b < _c.length; _b++) {
					var active = _c[_b];
					active.switchFlag = False;
				}
			}
			target.switchFlag = True;
			this.add('-activate', target, 'ability: Wimp Out');
		}
	""" 
	pass
