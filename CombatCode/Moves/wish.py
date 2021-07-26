def onStart(**bvalues):
	"""function (side, source) {
				this.effectData.hp = source.maxhp / 2;
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (side) {
				let target = side.active[this.effectData.sourcePosition];
				if (target && !target.fainted) {
					let source = this.effectData.source;
					let damage = this.heal(this.effectData.hp, target, target);
					if (damage) this.add('-heal', target, target.getHealth, '[from] move: Wish', '[wisher] ' + source.name);
				}
			}
	""" 
	pass
