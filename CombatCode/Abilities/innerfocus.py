def onTryAddVolatile(**bvalues):
	"""function (status, pokemon) {
			if (status.id === 'flinch')
				return null;
		}
	""" 
	pass

def onBoost(**bvalues):
	"""function (boost, target, source, effect) {
			if (effect.id === 'intimidate') {
				delete boost.atk;
				this.add('-fail', target, 'unboost', 'Attack', '[from] ability: Inner Focus', '[of] ' + target);
			}
		}
	""" 
	pass
