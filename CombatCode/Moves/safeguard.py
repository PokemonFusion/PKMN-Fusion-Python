def durationCallback(**bvalues):
	"""function (target, source, effect) {
				if (source && source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
				if (source && target !== source && effect && (!effect.infiltrates || target.side === source.side)) {
					this.debug('interrupting setStatus');
					if (effect.id === 'synchronize' || (effect.effectType === 'Move' && !effect.secondaries)) {
						this.add('-activate', target, 'move: Safeguard');
					}
					return null;
				}
			}
	""" 
	pass

def onTryAddVolatile(**bvalues):
	"""function (status, target, source, effect) {
				if ((status.id === 'confusion' || status.id === 'yawn') && source && target !== source && effect && (!effect.infiltrates || target.side === source.side)) {
					if (effect.effectType === 'Move' && !effect.secondaries) this.add('-activate', target, 'move: Safeguard');
					return null;
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'Safeguard');
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (side) {
				this.add('-sideend', side, 'Safeguard');
			}
	""" 
	pass
