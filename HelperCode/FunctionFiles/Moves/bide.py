def beforeMoveCallback (pokemon):
	"""function (pokemon) {
			if (pokemon.volatiles['bide'])
				return true;
		}
	""" 
	pass

def onBeforeMove (pokemon, target, move):
	"""function (pokemon, target, move) {
				if (this.effectState.duration === 1) {
					this.add('-end', pokemon, 'move: Bide');
					target = this.effectState.lastDamageSource;
					if (!target || !this.effectState.totalDamage) {
						this.attrLastMove('[still]');
						this.add('-fail', pokemon);
						return false;
					}
					if (!target.isActive) {
						var possibleTarget = this.getRandomTarget(pokemon, this.dex.moves.get('pound'));
						if (!possibleTarget) {
							this.add('-miss', pokemon);
							return false;
						}
						target = possibleTarget;
					}
					var moveData = {
						id: 'bide',
						name: "Bide",
						accuracy: true,
						damage: this.effectState.totalDamage * 2,
						category: "Physical",
						priority: 1,
						flags: { contact: 1, protect: 1 },
						effectType: 'Move',
						type: 'Normal',
					};
					this.actions.tryMoveHit(target, pokemon, moveData);
					pokemon.removeVolatile('bide');
					return false;
				}
				this.add('-activate', pokemon, 'move: Bide');
			}
	""" 
	pass

def onDamage (damage, target, source, move):
	"""function (damage, target, source, move) {
				if (!move || move.effectType !== 'Move' || !source)
					return;
				this.effectState.totalDamage += damage;
				this.effectState.lastDamageSource = source;
			}
	""" 
	pass

def onEnd (pokemon):
	"""function (pokemon) {
				this.add('-end', pokemon, 'move: Bide', '[silent]');
			}
	""" 
	pass

def onMoveAborted (pokemon):
	"""function (pokemon) {
				pokemon.removeVolatile('bide');
			}
	""" 
	pass

def onStart (pokemon):
	"""function (pokemon) {
				this.effectState.totalDamage = 0;
				this.add('-start', pokemon, 'move: Bide');
			}
	""" 
	pass