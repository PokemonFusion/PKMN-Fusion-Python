def onAllyBoost(**bvalues):
	"""function (boost, target, source, effect) {
			if ((source && target === source) || !target.hasType('Grass'))
				return;
			var showMsg = False;
			var i;
			for (i in boost) {
				if (boost[i] < 0) {
					delete boost[i];
					showMsg = True;
				}
			}
			if (showMsg && !effect.secondaries) {
				var effectHolder = this.effectState.target;
				this.add('-block', target, 'ability: Flower Veil', '[of] ' + effectHolder);
			}
		}
	""" 
	pass

def onAllySetStatus(**bvalues):
	"""function (status, target, source, effect) {
			if (target.hasType('Grass') && source && target !== source && effect && effect.id !== 'yawn') {
				this.debug('interrupting setStatus with Flower Veil');
				if (effect.id === 'synchronize' || (effect.effectType === 'Move' && !effect.secondaries)) {
					var effectHolder = this.effectState.target;
					this.add('-block', target, 'ability: Flower Veil', '[of] ' + effectHolder);
				}
				return null;
			}
		}
	""" 
	pass

def onAllyTryAddVolatile(**bvalues):
	"""function (status, target) {
			if (target.hasType('Grass') && status.id === 'yawn') {
				this.debug('Flower Veil blocking yawn');
				var effectHolder = this.effectState.target;
				this.add('-block', target, 'ability: Flower Veil', '[of] ' + effectHolder);
				return null;
			}
		}
	""" 
	pass
