def onEnd (target):
	"""function (target) {
				this.add('-end', target, 'Substitute');
			}
	""" 
	pass

def onStart (target):
	"""function (target) {
				this.add('-start', target, 'Substitute');
				this.effectState.hp = Math.floor(target.maxhp / 4);
				if (target.volatiles['partiallytrapped']) {
					this.add('-end', target, target.volatiles['partiallytrapped'].sourceEffect, '[partiallytrapped]', '[silent]');
					delete target.volatiles['partiallytrapped'];
				}
			}
	""" 
	pass

def onTryPrimaryHit (target, source, move):
	"""function (target, source, move) {
				if (target === source || move.flags['authentic'] || move.infiltrates) {
					return;
				}
				var damage = this.actions.getDamage(source, target, move);
				if (!damage && damage !== 0) {
					this.add('-fail', source);
					this.attrLastMove('[still]');
					return null;
				}
				damage = this.runEvent('SubDamage', target, source, move, damage);
				if (!damage) {
					return damage;
				}
				if (damage > target.volatiles['substitute'].hp) {
					damage = target.volatiles['substitute'].hp;
				}
				target.volatiles['substitute'].hp -= damage;
				source.lastDamage = damage;
				if (target.volatiles['substitute'].hp <= 0) {
					if (move.ohko)
						this.add('-ohko');
					target.removeVolatile('substitute');
				}
				else {
					this.add('-activate', target, 'move: Substitute', '[damage]');
				}
				if (move.recoil) {
					this.damage(this.actions.calcRecoilDamage(damage, move), source, target, 'recoil');
				}
				if (move.drain) {
					this.heal(Math.ceil(damage * move.drain[0] / move.drain[1]), source, target, 'drain');
				}
				this.singleEvent('AfterSubDamage', move, null, target, source, move, damage);
				this.runEvent('AfterSubDamage', target, source, move, damage);
				return this.HIT_SUBSTITUTE;
			}
	""" 
	pass

def onHit (target):
	"""function (target) {
			this.directDamage(target.maxhp / 4);
		}
	""" 
	pass

def onTryHit (target):
	"""function (target) {
			if (target.volatiles['substitute']) {
				this.add('-fail', target, 'move: Substitute');
				return null;
			}
			if (target.hp <= target.maxhp / 4 || target.maxhp === 1) { // Shedinja clause
				this.add('-fail', target, 'move: Substitute', '[weak]');
				return null;
			}
		}
	""" 
	pass