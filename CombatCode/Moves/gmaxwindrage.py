def onHit(**bvalues):
	"""function (source) {
				var success = false;
				var removeTarget = [
					'reflect', 'lightscreen', 'auroraveil', 'safeguard', 'mist', 'spikes', 'toxicspikes', 'stealthrock', 'stickyweb',
				];
				var removeAll = ['spikes', 'toxicspikes', 'stealthrock', 'stickyweb', 'gmaxsteelsurge'];
				for (var _i = 0, removeTarget_2 = removeTarget; _i < removeTarget_2.length; _i++) {
					var targetCondition = removeTarget_2[_i];
					if (source.side.foe.removeSideCondition(targetCondition)) {
						if (!removeAll.includes(targetCondition))
							continue;
						this.add('-sideend', source.side.foe, this.dex.conditions.get(targetCondition).name, '[from] move: G-Max Wind Rage', '[of] ' + source);
						success = true;
					}
				}
				for (var _a = 0, removeAll_2 = removeAll; _a < removeAll_2.length; _a++) {
					var sideCondition = removeAll_2[_a];
					if (source.side.removeSideCondition(sideCondition)) {
						this.add('-sideend', source.side, this.dex.conditions.get(sideCondition).name, '[from] move: G-Max Wind Rage', '[of] ' + source);
						success = true;
					}
				}
				this.field.clearTerrain();
				return success;
			}
	""" 
	pass
