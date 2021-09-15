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
        # if the pokemon is out of hp, it can't do anything
        if curpoke.pokemon.hp == 0:
            continue
        result = Result()
        if curpoke.turninit.attack is not None:
            result = damage_calc(curpoke.pokemon,
                                 turndata.positions[curpoke.getTarget()].pokemon,
                                 att,
                                 curpoke.getTarget(),
                                 curpoke.getAction())
            print(*result.text, sep="\n")
            print(result.debug.get("hp_percent", "Errored percent"))
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
            result.text.append(f"{att}.{newpoke.getName()} is changing places with {att}.{oldpoke.getName()}!")
            print(*result.text, sep="\n")



        elif curpoke.turninit.recharge:
            # TODO: Consider having the ability Truant flag for the message that is returned.
            pass

        elif curpoke.turninit.run:
            pass

    # This is where everything after the turn happens.
    for pos in battledata.turndata.positions:
        curpoke = battledata.turndata.positions[pos].pokemon
        stat = curpoke.getStatusName(True)

        def statNormal():
            pass  # intentionally do nothing

        def statBurn():
            """Take 1/16 of max hp in damage"""
            curpoke.modifyHP(-(curpoke.getStat("hp") / 16))
            print(f"{pos}.{curpoke.getName()} was damaged by burn!")


        statdic = {
            "NRM": statNormal,
            "BRN": statBurn,
        }

        statdic.get(stat, statNormal)()
        #because health was changed, we will need to check for new fainting

    print(f"Turn {battledata.battle.turn} ended")

    battledata.battle.incrementTurn()
    return fainted
