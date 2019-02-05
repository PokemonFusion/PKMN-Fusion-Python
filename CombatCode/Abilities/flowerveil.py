def onAllyBoost(datadic : dict):
	"""function (boost, target, source, effect) {
			if ((source && target === source) || !target.hasType('Grass')) return;
			let showMsg = false;
			for (let i in boost) {
				// @ts-ignore
				if (boost[i] < 0) {
					// @ts-ignore
					delete boost[i];
					showMsg = true;
				}
			}
			if (showMsg && !effect.secondaries) this.add('-fail', this.effectData.target, 'unboost', '[from] ability: Flower Veil', '[of] ' + target);
		}
	""" 
	pass

def onAllySetStatus(datadic : dict):
	"""function (status, target, source, effect) {
			if (target.hasType('Grass') && source && target !== source && effect) {
				this.debug('interrupting setStatus with Flower Veil');
				if (effect.id === 'synchronize' || (effect.effectType === 'Move' && !effect.secondaries)) {
					this.add('-activate', this.effectData.target, 'ability: Flower Veil', '[of] ' + target);
				}
				return null;
			}
		}
	""" 
	pass

def onAllyTryAddVolatile(datadic : dict):
	"""function (status, target) {
			if (target.hasType('Grass') && status.id === 'yawn') {
				this.debug('Flower Veil blocking yawn');
				this.add('-activate', this.effectData.target, 'ability: Flower Veil', '[of] ' + target);
				return null;
			}
		}
	""" 
	pass
