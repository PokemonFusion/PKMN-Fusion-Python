def onSourceTryHeal (damage, target, source, effect):
	"""function (damage, target, source, effect) {
			this.debug("Heal is occurring: " + target + " <- " + source + " :: " + effect.id);
			/**@type {{[k: string]: number}} */
			let canOoze = {drain: 1, leechseed: 1, strengthsap: 1};
			if (canOoze[effect.id]) {
				this.damage(damage);
				return 0;
			}
		}
	""" 
	pass