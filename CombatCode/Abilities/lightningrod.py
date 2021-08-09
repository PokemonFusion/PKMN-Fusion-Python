def onTryHit(**bvalues):
	"""function (target, source, move) {
			if (target !== source && move.type === 'Electric') {
				if (!this.boost({ spa: 1 })) {
					this.add('-immune', target, '[from] ability: Lightning Rod');
				}
				return null;
			}
		}
	""" 
	pass

def onAnyRedirectTarget(**bvalues):
	"""function (target, source, source2, move) {
			if (move.type !== 'Electric' || ['firepledge', 'grasspledge', 'waterpledge'].includes(move.id))
				return;
			var redirectTarget = ['randomNormal', 'adjacentFoe'].includes(move.target) ? 'normal' : move.target;
			if (this.validTarget(this.effectState.target, source, redirectTarget)) {
				if (move.smartTarget)
					move.smartTarget = False;
				if (this.effectState.target !== target) {
					this.add('-activate', this.effectState.target, 'ability: Lightning Rod');
				}
				return this.effectState.target;
			}
		}
	""" 
	pass
