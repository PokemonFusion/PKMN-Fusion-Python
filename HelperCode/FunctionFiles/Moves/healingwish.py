def onSwap (target):
	"""function (target) {
				if (!target.fainted && (target.hp < target.maxhp || target.status)) {
					target.heal(target.maxhp);
					target.setStatus('');
					this.add('-heal', target, target.getHealth, '[from] move: Healing Wish');
					target.side.removeSlotCondition(target, 'healingwish');
				}
			}
	""" 
	pass

def onTryHit (pokemon, target, move):
	"""function (pokemon, target, move) {
			if (!this.canSwitch(pokemon.side)) {
				delete move.selfdestruct;
				return false;
			}
		}
	""" 
	pass