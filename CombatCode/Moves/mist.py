def onBoost(**bvalues):
	"""function (boost, target, source, effect) {
				if (source && target !== source && (!effect.infiltrates || target.side === source.side)) {
					let showMsg = false;
					for (let i in boost) {
						// @ts-ignore
						if (boost[i] < 0) {
							// @ts-ignore
							delete boost[i];
							showMsg = true;
						}
					}
					if (showMsg && !effect.secondaries) this.add('-activate', target, 'move: Mist');
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (side) {
				this.add('-sidestart', side, 'Mist');
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (side) {
				this.add('-sideend', side, 'Mist');
			}
	""" 
	pass
