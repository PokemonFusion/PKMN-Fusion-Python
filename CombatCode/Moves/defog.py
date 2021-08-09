def onHit(**bvalues):
	"""function (target, source, move) {
			var success = false;
			if (!target.volatiles['substitute'] || move.infiltrates)
				success = !!this.boost({ evasion: -1 });
			var removeTarget = [
				'reflect', 'lightscreen', 'auroraveil', 'safeguard', 'mist', 'spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge',
			];
			var removeAll = [
				'spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge',
			];
			for (var _i = 0, removeTarget_1 = removeTarget; _i < removeTarget_1.length; _i++) {
				var targetCondition = removeTarget_1[_i];
				if (target.side.removeSideCondition(targetCondition)) {
					if (!removeAll.includes(targetCondition))
						continue;
					this.add('-sideend', target.side, this.dex.conditions.get(targetCondition).name, '[from] move: Defog', '[of] ' + source);
					success = true;
				}
			}
			for (var _a = 0, removeAll_1 = removeAll; _a < removeAll_1.length; _a++) {
				var sideCondition = removeAll_1[_a];
				if (source.side.removeSideCondition(sideCondition)) {
					this.add('-sideend', source.side, this.dex.conditions.get(sideCondition).name, '[from] move: Defog', '[of] ' + source);
					success = true;
				}
			}
			this.field.clearTerrain();
			return success;
		}
	""" 
	pass
