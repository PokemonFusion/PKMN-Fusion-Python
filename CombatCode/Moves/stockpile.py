def onTryHit(datadic : dict):
	"""function (pokemon) {
			if (pokemon.volatiles['stockpile'] && pokemon.volatiles['stockpile'].layers >= 3) return false;
		}
	""" 
	pass

def onStart(datadic : dict):
	"""function (target) {
				this.effectData.layers = 1;
				this.add('-start', target, 'stockpile' + this.effectData.layers);
				this.boost({def: 1, spd: 1}, target, target, this.getMove('stockpile'));
			}
	""" 
	pass

def onRestart(datadic : dict):
	"""function (target) {
				if (this.effectData.layers >= 3) return false;
				this.effectData.layers++;
				this.add('-start', target, 'stockpile' + this.effectData.layers);
				this.boost({def: 1, spd: 1}, target, target, this.getMove('stockpile'));
			}
	""" 
	pass

def onEnd(datadic : dict):
	"""function (target) {
				let layers = this.effectData.layers * -1;
				this.effectData.layers = 0;
				this.boost({def: layers, spd: layers}, target, target, this.getMove('stockpile'));
				this.add('-end', target, 'Stockpile');
			}
	""" 
	pass
