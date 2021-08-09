def onAnyTryMove(**bvalues):
	"""function (target, source, effect) {
			if (['explosion', 'mindblown', 'mistyexplosion', 'selfdestruct'].includes(effect.id)) {
				this.attrLastMove('[still]');
				this.add('cant', this.effectState.target, 'ability: Damp', effect, '[of] ' + target);
				return False;
			}
		}
	""" 
	pass

def onAnyDamage(**bvalues):
	"""function (damage, target, source, effect) {
			if (effect && effect.id === 'aftermath') {
				return False;
			}
		}
	""" 
	pass
