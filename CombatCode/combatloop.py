import CombatCode.pokeglobals as pglobals
from CombatCode.pokeglobals import Result
from CombatCode.battledata import TurnInit, BattleData, PositionData, DeclareAttack
from CombatCode.turnorder import calculateTurnorder
from CombatCode.damagecalculator import damage_calc


def combatloop(battledata: BattleData) -> list:
    """Does the combat loop and returns a list of the fainted pokemon"""
    turndata = battledata.turndata
    turnorder = calculateTurnorder(turndata)
    fainted = []
    for att in turnorder:
        curpoke = turndata.positions[att]
        result = Result()
        if curpoke.turninit.attack is not None:
            result = damage_calc(curpoke.pokemon,
                                 turndata.positions[curpoke.getTarget()].pokemon,
                                 att,
                                 curpoke.getTarget(),
                                 curpoke.getAction())
            print(result.text)
            print(result.debug["hp_percent"])
            if len(result.fainted) > 0:
                fainted += result.fainted
        elif curpoke.turninit.item is not None:
            # Run this if the position is using an item
            pass
        elif curpoke.turninit.switch is not None:
            # Run this if the position is going to be switched
            slot = curpoke.turninit.switch
            team = att[0]
            newpoke = battledata.teams[team].returndict()[slot]
            oldpoke = curpoke.pokemon
            turndata.positions[att].pokemon = newpoke
            result.text = f"{att}.{newpoke.getName()} is changing places with {att}.{oldpoke.getName()}!"
            print(result.text)



        elif curpoke.turninit.recharge:
            # TODO: Consider having the ability Truant flag for the message that is returned.
            pass

        elif curpoke.turninit.run:
            pass

    return fainted
