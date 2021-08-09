def onSetStatus (status, target, source, effect):
	"""function (status, target, source, effect) {
			var _a;
			if (['sunnyday', 'desolateland'].includes(target.effectiveWeather())) {
				if ((_a = effect) === null || _a === void 0 ? void 0 : _a.status) {
					this.add('-immune', target, '[from] ability: Leaf Guard');
				}
				return False;
			}
		}
	""" 
	pass

def onTryAddVolatile (status, target):
	"""function (status, target) {
			if (status.id === 'yawn' && ['sunnyday', 'desolateland'].includes(target.effectiveWeather())) {
				this.add('-immune', target, '[from] ability: Leaf Guard');
				return null;
			}
		}
	""" 
	pass