import random
from math import floor
from CombatCode.pokeglobals import Moves, Result
from CombatCode.elements import ElementEffectiveness as TypeEff
from CombatCode.battledata import Pokemon
from CombatCode.movesdex import BattleMovedex
from CombatCode.abilitiesdex import BattleAbilities
from CombatCode.pokemon import STATUSES_REVERSE_SHORT

"""
 Assumptions:

 The current version will be using a dictionary for the data

 Current template:

 BattleData = { "teams" : { "A" : { 1 : {*Pokemon information/stats*}} },
                "battle" : {},
                "turn" : { "position" : { "field-A1" : 1  } }
 }

 Update: 11/28/2018
    Decided to go with a class instead of a dictionary the class is in the battledata.py file


"""

MULTIHITCOUNT = {2: 3,
                 3: 3,
                 4: 1,
                 5: 1}

def percent_check(check) -> bool:
	"""Enter a number between 0.0 and 1.0.
	A random float will be generated 0.0 <= x < 1.0.
	If the number being checked is larger return True, else False"""
	return check > random.random()


def accuracy_check(attacker, target, move) -> bool:
	"""This will return if an attack hits or misses the target"""
	# place holders, but we will want to use classes for each properly
	attacc = attacker.checkAcc()
	tareva = target.checkEvade()
	moveacc = move.accuracy
	if move.accuracy is True:
		return True
	tohit = (moveacc * (attacc/tareva)) / 100
	return percent_check(tohit)


def critical_hit_check(attacker, move) -> bool:
	"""This will return if an attack is a crit or a regular hit"""
	critstage = attacker.checkCrit(move.critRatio)

	# just because I can, I'm going to make a switch statement here

	critdic = {0: 1/24, 1: 1/8, 2: 1/2}
	critper = critdic.get(critstage, 1)

	return percent_check(critper)


def base_damage(level, basePower, attackStat, defenseStat) -> int:
	"""Damage before modifiers"""
	damage = (floor(floor(floor(((2 * level) / 5) + 2) * basePower * (attackStat * 1.0) /
	                      defenseStat) / 50) + 2)
	randMod = random.randint(85, 100)/100.0
	return floor(damage * randMod)


def STAB(attacker, move: Moves) -> float:
	atypes = attacker.getTypes()
	if move.type in atypes:
		# TODO: adaptibility goes here, maybe?
		return 1.5
	else:
		return 1.0


def elementTypeTotal(target, move: Moves) -> float:
	types = target.getTypes() # make/use a method in case there are abilities that would change this
	effect = 1.0
	for ptype in types:
		effect = effect * (TypeEff[move.type.lower()][ptype.lower()] / 100.0)

	return effect


def damagephrase(target, damage) -> str:
	maxhp = target.getStat("hp")

	def dam_name(damage_percent) -> str:
		if damage_percent >= 100:
			return "EPIC"
		elif damage_percent > 75:
			return "extreme"
		elif damage_percent > 50:
			return "heavy"
		elif damage_percent > 25:
			return "considerable"
		elif damage_percent > 15:
			return "moderate"
		elif damage_percent > 5:
			return "light"
		elif damage_percent > 0:
			return "puny"
		else:
			return "no"
	return dam_name((damage * 100) / maxhp)


def damage_calc(attacker: Pokemon, target: Pokemon, attackerpos, targetpos, move: Moves) -> Result:
	"""Use this for calculating damage fully"""
	# Initial version of this will heavily reference the way I (Yang/Koden) had coded it in MUF
	result = Result()
	numhits = 1
	if isinstance(move.multihit, list):
		population, weights = zip(*MULTIHITCOUNT.items())
		numhits = random.choices(population, weights)[0]
	elif move.multihit is not None:
		numhits = move.multihit

	attname = "{}.{}".format(attackerpos, attacker.getName())
	tarname = "{}.{}".format(targetpos, target.getName())

	for _ in range(numhits):
		# around here I think is where we would be calling any 'onModifyMove' flags for the ability or move involved

		# begin by checking accuracy
		if accuracy_check(attacker, target, move):
			onHit = target.getAbility().onHit
			if onHit is not None:
				onHit(pokemon=attacker, target=target, move=move, result=result, attname=attname, tarname=tarname)

			onHit = move.onHit
			if onHit is not None:
				onHit(pokemon=attacker, target=target, move=move, result=result, attname=attname, tarname=tarname)

			crit = 1
			if move.category != 'Status':

				isCrit = False
				if critical_hit_check(attacker, move):
					crit = 1.5  # TODO: Criticals ignore def boots and atk drops, except for burn
					isCrit = True
				attackStat = 0
				defenseStat = 0
				if move.category == 'Physical':
					attackStat = attacker.getStat("atk", isCrit)
					defenseStat = target.getStat("def", isCrit)

				elif move.category == 'Special':
					attackStat = attacker.getStat("spa", isCrit)
					defenseStat = target.getStat("spd", isCrit)

				basedamage = base_damage(
					attacker.level, move.calculateBasePower(pokemon=attacker, target=target, move=move), attackStat, defenseStat)

				# TODO: figure out where to put 'onUseMoveMessage' functions.
				damage = basedamage * STAB(attacker, move)
				typetotal = elementTypeTotal(target, move)  # hold on to typetotal for the super effective print
				damage = floor(damage * typetotal * crit)
				phrase = damagephrase(target, damage)

				# TODO: Substitute would go somewhere around here I think
				current_hp = target.takeDamage(damage)
				if current_hp == 0:
					result.fainted.append(targetpos)

				result.debug['damage'] = damage
				result.debug['current_hp'] = current_hp
				result.debug['hp_percent'] = current_hp/target.getStat("hp")

				effectivePhrase = ""

				if typetotal > 1:
					effectivePhrase = "it's SUPER EFFECTIVE"
					if typetotal > 2:
						effectivePhrase += " x2"
				elif typetotal == 0:
					effectivePhrase = "they are immune..."
				elif typetotal < 1:
					effectivePhrase = "it's not very effective..."
					if typetotal < 0.5:
						effectivePhrase += " x2"
				critphrase = ""
				if crit > 1:
					critphrase = " CRITICAL"  # mind the space

				if damage > 0:
					target.tempvals['hurtThisTurn'] = True
					target.tempvals.setdefault('attackers', []).append(attackerpos)

				result.text.append(\
					"{attname} uses {movename} against {tarname}, {effective}and deals {damphrase}{crit} damage!".format(
						attname=attname,
						tarname=tarname, effective=effectivePhrase,
						movename=move.name, damphrase=phrase, crit=critphrase
					))
				if current_hp == 0:
					result.text.append("{tarname} fainted!".format(tarname="{}.{}".format(targetpos, target.getName())))
			else: #catetory == 'Status'
				# We will add to this as needed.
				boosts = move.get("boosts")
				if boosts:
					for boost in boosts:
						move.target

				# Put secondary effects here
			if move.secondary:
				if move.secondary.get('status') and target.status["name"] != 0: # can't change status if there is one
					status = move.secondary.get('status').capitalize()
					chance = move.secondary.get('chance', 100)
					if percent_check(chance/100):
						target.setStatus(STATUSES_REVERSE_SHORT[status])




		else:
			result.text.append("{attname} uses {movename} against {tarname} but it missed!".format(
				attname=attname, movename=move.name, tarname=tarname))

	if numhits > 1:
		result.text.append("{attname} attacked {numhits} times!".format(
			attname=attname,
			numhits=numhits
		))

	result.debug['hp_percent'] = current_hp / target.getStat("hp")
	return result
