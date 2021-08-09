def onBoost(**bvalues):
	"""function (boost, target, source, effect) {
				if (effect.effectType === 'Move' && effect.infiltrates && !target.isAlly(source))
					return;
				if (source && target !== source) {
					var showMsg = false;
					var i = void 0;
					for (i in boost) {
						if (boost[i] < 0) {
							delete boost[i];
							showMsg = true;
						}
					}
					if (showMsg && !effect.secondaries) {
						this.add('-activate', target, 'move: Mist');
					}
				}
			}
	""" 
	pass

def onSideEnd(**bvalues):
	"""function (side) {
				this.add('-sideend', side, 'Mist');
			}
	""" 
	pass

def onSideStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'Mist');
			}
	""" 
	pass
