def durationCallback(**bvalues):
	"""function (target, source, effect) {
				if (source === null || source === void 0 ? void 0 : source.hasAbility('persistent')) {
					this.add('-activate', source, 'ability: Persistent', effect);
					return 7;
				}
				return 5;
			}
	""" 
	pass

def onSetStatus(**bvalues):
	"""function (status, target, source, effect) {
				if (!effect || !source)
					return;
				if (effect.id === 'yawn')
					return;
				if (effect.effectType === 'Move' && effect.infiltrates && !target.isAlly(source))
					return;
				if (target !== source) {
					this.debug('interrupting setStatus');
					if (effect.id === 'synchronize' || (effect.effectType === 'Move' && !effect.secondaries)) {
						this.add('-activate', target, 'move: Safeguard');
					}
					return null;
				}
			}
	""" 
	pass

def onSideEnd(**bvalues):
	"""function (side) {
				this.add('-sideend', side, 'Safeguard');
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'Safeguard');
			}
	""" 
	pass

def onTryAddVolatile(**bvalues):
	"""function (status, target, source, effect) {
				if (!effect || !source)
					return;
				if (effect.effectType === 'Move' && effect.infiltrates && !target.isAlly(source))
					return;
				if ((status.id === 'confusion' || status.id === 'yawn') && target !== source) {
					if (effect.effectType === 'Move' && !effect.secondaries)
						this.add('-activate', target, 'move: Safeguard');
					return null;
				}
			}
	""" 
	pass
