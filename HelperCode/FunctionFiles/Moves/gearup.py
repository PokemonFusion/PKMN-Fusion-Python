def onHitSide (side, source, move):
	"""function (side, source, move) {
			var _this = this;
			var targets = side.allies().filter(function (target) { return (target.hasAbility(['plus', 'minus']) &&
				(!target.volatiles['maxguard'] || _this.runEvent('TryHit', target, source, move))); });
			if (!targets.length)
				return false;
			var didSomething = false;
			for (var _i = 0, targets_2 = targets; _i < targets_2.length; _i++) {
				var target = targets_2[_i];
				didSomething = this.boost({ atk: 1, spa: 1 }, target, source, move, false, true) || didSomething;
			}
			return didSomething;
		}
	""" 
	pass