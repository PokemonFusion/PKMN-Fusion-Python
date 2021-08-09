def onEnd(**bvalues):
	"""function (target) {
				if (target && !target.fainted) {
					var damage = this.heal(this.effectState.hp, target, target);
					if (damage) {
						this.add('-heal', target, target.getHealth, '[from] move: Wish', '[wisher] ' + this.effectState.source.name);
					}
				}
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon, source) {
				this.effectState.hp = source.maxhp / 2;
			}
	""" 
	pass
