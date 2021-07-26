def onAnyTryMove(**bvalues):
	"""function (target, source, effect) {
			if (['explosion', 'mindblown', 'selfdestruct'].includes(effect.id)) {
				this.attrLastMove('[still]');
				this.add('cant', this.effectData.target, 'ability: Damp', effect, '[of] ' + target);
				return false;
			}
		}
	""" 
	pass

def onAnyDamage(**bvalues):
	"""function (damage, target, source, effect) {
			if (effect && effect.id === 'aftermath') {
				return false;
			}
		}
	""" 
	pass
