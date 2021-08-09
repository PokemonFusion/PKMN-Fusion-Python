def onHitField(**bvalues):
	"""function (target, source) {
			var _a, _b;
			var sideConditions = [
				'mist', 'lightscreen', 'reflect', 'spikes', 'safeguard', 'tailwind', 'toxicspikes', 'stealthrock', 'waterpledge', 'firepledge', 'grasspledge', 'stickyweb', 'auroraveil', 'gmaxsteelsurge', 'gmaxcannonade', 'gmaxvinelash', 'gmaxwildfire',
			];
			var success = false;
			if (this.gameType === "freeforall") {
				// random integer from 1-3 inclusive
				var offset = this.random(3) + 1;
				// the list of all sides in counterclockwise order
				var sides = [this.sides[0], this.sides[2], this.sides[1], this.sides[3]];
				for (var _i = 0, sideConditions_1 = sideConditions; _i < sideConditions_1.length; _i++) {
					var id = sideConditions_1[_i];
					var effectName = this.dex.conditions.get(id).name;
					var rotatedSides = [];
					var someCondition = false;
					for (var i = 0; i < 4; i++) {
						var sourceSide = sides[i];
						var targetSide = sides[(i + offset) % 4]; // the next side in rotation
						rotatedSides.push(targetSide.sideConditions[id]);
						if (sourceSide.sideConditions[id]) {
							this.add('-sideend', sourceSide, effectName, '[silent]');
							someCondition = true;
						}
					}
					if (!someCondition)
						continue;
					_a = __spreadArrays(rotatedSides), sides[0].sideConditions[id] = _a[0], sides[1].sideConditions[id] = _a[1], sides[2].sideConditions[id] = _a[2], sides[3].sideConditions[id] = _a[3];
					for (var _c = 0, sides_1 = sides; _c < sides_1.length; _c++) {
						var side = sides_1[_c];
						if (side.sideConditions[id]) {
							var layers = side.sideConditions[id].layers || 1;
							for (; layers > 0; layers--)
								this.add('-sidestart', side, effectName, '[silent]');
						}
						else {
							delete side.sideConditions[id];
						}
					}
					success = true;
				}
			}
			else {
				var sourceSide = source.side;
				var targetSide = source.side.foe;
				for (var _d = 0, sideConditions_2 = sideConditions; _d < sideConditions_2.length; _d++) {
					var id = sideConditions_2[_d];
					var effectName = this.dex.conditions.get(id).name;
					if (sourceSide.sideConditions[id] && targetSide.sideConditions[id]) {
						_b = [
							targetSide.sideConditions[id], sourceSide.sideConditions[id],
						], sourceSide.sideConditions[id] = _b[0], targetSide.sideConditions[id] = _b[1];
						this.add('-sideend', sourceSide, effectName, '[silent]');
						this.add('-sideend', targetSide, effectName, '[silent]');
					}
					else if (sourceSide.sideConditions[id] && !targetSide.sideConditions[id]) {
						targetSide.sideConditions[id] = sourceSide.sideConditions[id];
						delete sourceSide.sideConditions[id];
						this.add('-sideend', sourceSide, effectName, '[silent]');
					}
					else if (targetSide.sideConditions[id] && !sourceSide.sideConditions[id]) {
						sourceSide.sideConditions[id] = targetSide.sideConditions[id];
						delete targetSide.sideConditions[id];
						this.add('-sideend', targetSide, effectName, '[silent]');
					}
					else {
						continue;
					}
					var sourceLayers = sourceSide.sideConditions[id] ? (sourceSide.sideConditions[id].layers || 1) : 0;
					var targetLayers = targetSide.sideConditions[id] ? (targetSide.sideConditions[id].layers || 1) : 0;
					for (; sourceLayers > 0; sourceLayers--) {
						this.add('-sidestart', sourceSide, effectName, '[silent]');
					}
					for (; targetLayers > 0; targetLayers--) {
						this.add('-sidestart', targetSide, effectName, '[silent]');
					}
					success = true;
				}
			}
			if (!success)
				return false;
			this.add('-activate', source, 'move: Court Change');
		}
	""" 
	pass
