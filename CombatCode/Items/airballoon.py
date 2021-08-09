def onAfterSubDamage(**bvalues):
	"""function (damage, target, source, effect) {
			this.debug('effect: ' + effect.id);
			if (effect.effectType === 'Move') {
				this.add('-enditem', target, 'Air Balloon');
				target.item = '';
				target.itemState = { id: '', target: target };
				this.runEvent('AfterUseItem', target, null, null, this.dex.items.get('airballoon'));
			}
		}
	""" 
	pass

def onDamagingHit(**bvalues):
	"""function (damage, target, source, move) {
			this.add('-enditem', target, 'Air Balloon');
			target.item = '';
			target.itemState = { id: '', target: target };
			this.runEvent('AfterUseItem', target, null, null, this.dex.items.get('airballoon'));
		}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
			if (!target.ignoringItem() && !this.field.getPseudoWeather('gravity')) {
				this.add('-item', target, 'Air Balloon');
			}
		}
	""" 
	pass
