def onHitSide(**bvalues):
	"""function (side, source, move) {
			var _this = this;
			var targets = side.allies().filter(function (ally) { return (ally.hasAbility(['plus', 'minus']) &&
				(!ally.volatiles['maxguard'] || _this.runEvent('TryHit', ally, source, move))); });
			if (!targets.length)
				return false;
			var didSomething = false;
			for (var _i = 0, targets_3 = targets; _i < targets_3.length; _i++) {
				var target = targets_3[_i];
				didSomething = this.boost({ def: 1, spd: 1 }, target, source, move, false, true) || didSomething;
			}
			return didSomething;
		}
	""" 
	pass
