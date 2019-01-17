import random
from math import floor
from CombatCode.pokeglobals import Moves, Result
from CombatCode.elements import ElementEffectiveness as TypeEff

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


def percent_check(check) -> bool:
    if check <= random.rancom():
        return True
    else:
        return False


def accuracy_check(attacker, target, move) -> bool:
    """This will return if an attack hits or misses the target"""
    # place holders, but we will want to use classes for each properly
    attacc = attacker.checkAcc()
    tareva = target.checkEvade()
    moveacc = move.accuracy
    if move.accuracy == True:
        return True
    tohit = moveacc * (attacc/tareva)
    return percent_check(tohit)


def critical_hit_check(attacker) -> bool:
    """This will return if an attack is a crit or a miss"""
    critstage = attacker.checkCrit()

    # just because I can, I'm going to make a switch statement here

    critdic = {0: 1/24, 1: 1/8, 2: 1/2}
    critper = critdic.get(critstage, 1)

    return percent_check(critper)


def base_damage(level, basePower, attackStat, defenseStat) -> int:
    """Damage before modifiers"""
    damage = ((((((2 * level) / 5) + 2) * basePower * (attackStat * 1.0) /
                defenseStat) / 50) + 2)
    randMod = random.randint(85, 100)/100.0
    return int(damage * randMod)

def STAB(attacker, move: Moves) -> float:
    atypes = attacker.types()
    if move.type in atypes:
        #TODO: adaptibility goes here
        return 1.5
    else:
        return 1.0

def elementTypeTotal(target, move:Moves) -> float:
    types = target.getTypes() #make/use a method in case there are abilities that would change this
    effect = 1.0
    for ptype in types:
        effect = effect * (TypeEff[move.type][ptype] / 100.0)

    return effect

def damage_calc(attacker, target, move: Moves) -> Result:
    """Use this for calculating damage fully"""
    # Initial version of this will heavily reference the way I (Yang/Koden) had coded it in MUF
    result = Result()
    # around here I think is where we would be calling any 'onModifyMove' flags for the ability or move involved

    # begin by checking accuracy
    if accuracy_check(attacker, target, move):
        crit = 1
        if critical_hit_check(attacker):
            crit = 1.5

        attackStat = 0
        defenseStat = 0

        if move.category == 'Physical':
            attackStat = attacker.calculatePhyAtk()
            defenseStat = target.calculatePhyDef()

        elif move.category == 'Special':
            attackStat = attacker.calculateSpcAtk()
            defenseStat = target.calculateSpcDef()

        basedamage = base_damage(
            attacker.level, move.calculateBasePower(), attackStat, defenseStat)
        
        #TODO: figure out where to put 'onUseMoveMessage' functions.
        damage = basedamage * STAB(attacker, move)
        typetotal = elementTypeTotal(target, move) 

    else:
        # TODO: return something for when fails
        result.text = "{attname} uses {movename} on {tarname} but it missed!".format(attname="{}.{}".format(
            attacker.position, attacker.name), movename=move.name, tarname="{}.{}".format(target.position, target.name))

    return result
