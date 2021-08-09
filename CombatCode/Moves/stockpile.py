def onEnd(**bvalues):
	"""function (target) {
				if (this.effectState.def || this.effectState.spd) {
					var boosts = {};
					if (this.effectState.def)
						boosts.def = this.effectState.def;
					if (this.effectState.spd)
						boosts.spd = this.effectState.spd;
					this.boost(boosts, target, target);
				}
				this.add('-end', target, 'Stockpile');
				if (this.effectState.def !== this.effectState.layers * -1 || this.effectState.spd !== this.effectState.layers * -1) {
					this.hint("In Gen 7, Stockpile keeps track of how many times it successfully altered each stat individually.");
				}
			}
	""" 
	pass

def onRestart(**bvalues):
	"""function (target) {
				if (this.effectState.layers >= 3)
					return false;
				this.effectState.layers++;
				this.add('-start', target, 'stockpile' + this.effectState.layers);
				var curDef = target.boosts.def;
				var curSpD = target.boosts.spd;
				this.boost({ def: 1, spd: 1 }, target, target);
				if (curDef !== target.boosts.def)
					this.effectState.def--;
				if (curSpD !== target.boosts.spd)
					this.effectState.spd--;
			}
	""" 
	pass

def onStart(**bvalues):
	"""function (target) {
				this.effectState.layers = 1;
				this.effectState.def = 0;
				this.effectState.spd = 0;
				this.add('-start', target, 'stockpile' + this.effectState.layers);
				var _a = [target.boosts.def, target.boosts.spd], curDef = _a[0], curSpD = _a[1];
				this.boost({ def: 1, spd: 1 }, target, target);
				if (curDef !== target.boosts.def)
					this.effectState.def--;
				if (curSpD !== target.boosts.spd)
					this.effectState.spd--;
			}
	""" 
	pass

def onTry(**bvalues):
	"""function (source) {
			if (source.volatiles['stockpile'] && source.volatiles['stockpile'].layers >= 3)
				return false;
		}
	""" 
	pass
