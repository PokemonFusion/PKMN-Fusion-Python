def onSwap(**bvalues):
	"""function (target) {
				if (!target.fainted && (target.hp < target.maxhp ||
					target.status ||
					target.moveSlots.some(function (moveSlot) { return moveSlot.pp < moveSlot.maxpp; }))) {
					target.heal(target.maxhp);
					target.setStatus('');
					for (var _i = 0, _a = target.moveSlots; _i < _a.length; _i++) {
						var moveSlot = _a[_i];
						moveSlot.pp = moveSlot.maxpp;
					}
					this.add('-heal', target, target.getHealth, '[from] move: Lunar Dance');
					target.side.removeSlotCondition(target, 'lunardance');
				}
			}
	""" 
	pass

def onTryHit(**bvalues):
	"""function (pokemon, target, move) {
			if (!this.canSwitch(pokemon.side)) {
				delete move.selfdestruct;
				return false;
			}
		}
	""" 
	pass
