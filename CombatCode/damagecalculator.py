import random
from math import floor
from CombatCode.pokeglobals import Moves, Result
from CombatCode.elements import ElementEffectiveness as TypeEff
from CombatCode.battledata import Pokemon

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
datadic = {}


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
    """This will return if an attack is a crit or a miss"""
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


def damage_calc(attacker: Pokemon, target: Pokemon, move: Moves) -> Result:
    """Use this for calculating damage fully"""
    # Initial version of this will heavily reference the way I (Yang/Koden) had coded it in MUF
    result = Result()

    datadic['pokemon'] = attacker
    datadic['target'] = target
    datadic['move'] = move

    # around here I think is where we would be calling any 'onModifyMove' flags for the ability or move involved

    # begin by checking accuracy
    if accuracy_check(attacker, target, move):
        crit = 1
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
            attacker.level, move.calculateBasePower(datadic), attackStat, defenseStat)
        
        # TODO: figure out where to put 'onUseMoveMessage' functions.
        damage = basedamage * STAB(attacker, move)
        typetotal = elementTypeTotal(target, move) # hold on to typetotal for the super effective print
        damage = floor(damage * typetotal * crit)
        phrase = damagephrase(target, damage)

        # TODO: Substitute would go somewhere around here I think
        curhp = target.takeDamage(damage)
        if curhp == 0:
            result.fainted.append(target.getPosition())

        result.debug['damage'] = damage
        result.debug['curhp'] = curhp
        result.debug['hp_percent'] = curhp/target.getStat("hp")

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
            target.tempvals.setdefault('attackers', []).append(attacker.getPosition())

        result.text = \
            "{attname} uses {movename} against {tarname}, {effective}and deals {damphrase}{crit} damage!".format(
                attname="{}.{}".format(attacker.getPosition(), attacker.getName()),
                tarname="{}.{}".format(target.getPosition(), target.getName()), effective=effectivePhrase,
                movename=move.name, damphrase=phrase, crit=critphrase
            )

    else:
        result.text = "{attname} uses {movename} against {tarname} but it missed!".format(attname="{}.{}".format(
            attacker.getPosition(), attacker.getName()), movename=move.name, tarname="{}.{}".format(target.position, target.getName))

    return result
