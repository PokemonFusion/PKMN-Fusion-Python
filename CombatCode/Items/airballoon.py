def onStart(**bvalues):
	"""function (target) {
			if (!target.ignoringItem() && !this.getPseudoWeather('gravity')) {
				this.add('-item', target, 'Air Balloon');
			}
		}
	""" 
	pass

def onAfterDamage(**bvalues):
	"""function (damage, target, source, effect) {
			this.debug('effect: ' + effect.id);
			if (effect.effectType === 'Move' && effect.id !== 'confused') {
				this.add('-enditem', target, 'Air Balloon');
				target.item = '';
				this.itemData = {id: '', target: this};
				this.runEvent('AfterUseItem', target, null, null, 'airballoon');
			}
		}
	""" 
	pass

def onAfterSubDamage(**bvalues):
	"""function (damage, target, source, effect) {
			this.debug('effect: ' + effect.id);
			if (effect.effectType === 'Move' && effect.id !== 'confused') {
				this.add('-enditem', target, 'Air Balloon');
				target.item = '';
				this.itemData = {id: '', target: this};
				this.runEvent('AfterUseItem', target, null, null, 'airballoon');
			}
		}
	""" 
	pass
