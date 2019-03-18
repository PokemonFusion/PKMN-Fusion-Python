import CombatCode.pokeglobals as pglobals
from CombatCode.pokeglobals import Result
from CombatCode.battledata import TurnInit, TurnData, PositionData, DeclareAttack
from CombatCode.turnorder import calculateTurnorder
from CombatCode.damagecalculator import damage_calc


def combatloop(battledata: TurnData):
    battle = True
    while battle:
        turnorder = calculateTurnorder(battledata)
        for att in turnorder:
            curpoke = battledata.positions[att]
            # result = Result()
            if curpoke.turninit.attack is not None:
                result = damage_calc(curpoke.pokemon, battledata.positions[curpoke.getTarget()].pokemon,
                                     curpoke.getAction())
                print(result.text)
                print(result.debug["hp_percent"])

            if len(result.fainted) > 0:
                battle = False
                break
