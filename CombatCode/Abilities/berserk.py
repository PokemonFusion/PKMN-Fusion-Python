def onDamage(**bvalues):
	"""function (damage, target, source, effect) {
			if (effect.effectType === "Move" &&
				!effect.multihit &&
				(!effect.negateSecondary && !(effect.hasSheerForce && source.hasAbility('sheerforce')))) {
				target.abilityState.checkedBerserk = False;
			}
			else {
				target.abilityState.checkedBerserk = True;
			}
		}
	""" 
	pass

def onTryEatItem(**bvalues):
	"""function (item, pokemon) {
			var healingItems = [
				'aguavberry', 'enigmaberry', 'figyberry', 'iapapaberry', 'magoberry', 'sitrusberry', 'wikiberry', 'oranberry', 'berryjuice',
			];
			if (healingItems.includes(item.id)) {
				return pokemon.abilityState.checkedBerserk;
			}
			return True;
		}
	""" 
	pass

def onAfterMoveSecondary(**bvalues):
	"""function (target, source, move) {
			target.abilityState.checkedBerserk = True;
			if (!source || source === target || !target.hp || !move.totalDamage)
				return;
			var lastAttackedBy = target.getLastAttackedBy();
			if (!lastAttackedBy)
				return;
			var damage = move.multihit ? move.totalDamage : lastAttackedBy.damage;
			if (target.hp <= target.maxhp / 2 && target.hp + damage > target.maxhp / 2) {
				this.boost({ spa: 1 });
			}
		}
	""" 
	pass
