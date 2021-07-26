def beforeMoveCallback(**bvalues):
	"""function (pokemon) {
			if (pokemon.volatiles['bide']) return true;
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (pokemon) {
				this.effectData.totalDamage = 0;
				this.add('-start', pokemon, 'move: Bide');
			}
	""" 
	pass

def onDamage(**bvalues):
	"""function (damage, target, source, move) {
				if (!move || move.effectType !== 'Move' || !source) return;
				this.effectData.totalDamage += damage;
				this.effectData.lastDamageSource = source;
			}
	""" 
	pass

def onBeforeMove(**bvalues):
	"""function (pokemon, target, move) {
				if (this.effectData.duration === 1) {
					this.add('-end', pokemon, 'move: Bide');
					target = this.effectData.lastDamageSource;
					if (!target || !this.effectData.totalDamage) {
						this.attrLastMove('[still]');
						this.add('-fail', pokemon);
						return false;
					}
					if (!target.isActive) target = this.resolveTarget(pokemon, this.getMove('pound'));
					if (!this.isAdjacent(pokemon, target)) {
						this.add('-miss', pokemon, target);
						return false;
					}
					let moveData = {
						id: 'bide',
						name: "Bide",
						accuracy: true,
						damage: this.effectData.totalDamage * 2,
						category: "Physical",
						priority: 1,
						flags: {contact: 1, protect: 1},
						effectType: 'Move',
						type: 'Normal',
					};
					// @ts-ignore
					this.tryMoveHit(target, pokemon, moveData);
					return false;
				}
				this.add('-activate', pokemon, 'move: Bide');
			}
	""" 
	pass

def onMoveAborted(**bvalues):
	"""function (pokemon) {
				pokemon.removeVolatile('bide');
			}
	""" 
	pass

def onEnd(**bvalues):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Bide', '[silent]');
			}
	""" 
	pass
