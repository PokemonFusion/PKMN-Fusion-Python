def onModifyCritRatio(**bvalues):
	"""function (critRatio) {
				return critRatio + this.effectState.layers;
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (target, source, effect) {
				if (this.effectState.layers >= 3)
					return false;
				this.effectState.layers++;
				if (!['imposter', 'psychup', 'transform'].includes(effect === null || effect === void 0 ? void 0 : effect.id)) {
					this.add('-start', target, 'move: G-Max Chi Strike');
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target, source, effect) {
				this.effectState.layers = 1;
				if (!['imposter', 'psychup', 'transform'].includes(effect === null || effect === void 0 ? void 0 : effect.id)) {
					this.add('-start', target, 'move: G-Max Chi Strike');
				}
			}
	""" 
	pass

def onHit(**bvalues):
	"""function (source) {
				for (var _i = 0, _a = source.alliesAndSelf(); _i < _a.length; _i++) {
					var pokemon = _a[_i];
					pokemon.addVolatile('gmaxchistrike');
				}
			}
	""" 
	pass
