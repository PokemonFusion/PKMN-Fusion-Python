def onDamagingHit(**bvalues):
	"""function (damage, target, source, move) {
			if (!source.hp || !source.isActive || target.transformed || target.isSemiInvulnerable())
				return;
			if (['cramorantgulping', 'cramorantgorging'].includes(target.species.id)) {
				this.damage(source.baseMaxhp / 4, source, target);
				if (target.species.id === 'cramorantgulping') {
					this.boost({ def: -1 }, source, target, null, True);
				}
				else {
					source.trySetStatus('par', target, move);
				}
				target.formeChange('cramorant', move);
			}
		}
	""" 
	pass

def onSourceTryPrimaryHit(**bvalues):
	"""function (target, source, effect) {
			if (effect && effect.id === 'surf' && source.hasAbility('gulpmissile') &&
				source.species.name === 'Cramorant' && !source.transformed) {
				var forme = source.hp <= source.maxhp / 2 ? 'cramorantgorging' : 'cramorantgulping';
				source.formeChange(forme, effect);
			}
		}
	""" 
	pass
