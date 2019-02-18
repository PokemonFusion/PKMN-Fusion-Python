import CombatCode.pokeglobals as pglobals
from CombatCode.battledata import TurnInit
import CombatCode.battledata
from CombatCode.turnorder import calculateTurnorder
from CombatCode.damagecalculator import damage_calc

testbattle = CombatCode.battledata.TurnData()
testbattle.positions = dict()
testbattle.positions["A1"] = CombatCode.battledata.PositionData()
A1 = testbattle.positions["A1"]
A1.pokemon = CombatCode.battledata.Pokemon(1,"A",1,"pikachu", level=50)

A1.turninit = TurnInit(attack=CombatCode.battledata.DeclareAttack('B1', pglobals.Moves("tackle")))
testbattle.positions["B1"] = CombatCode.battledata.TurnData()
B1 = testbattle.positions["B1"]
B1.pokemon = CombatCode.battledata.Pokemon(1,"B",1,"hitmonchan",level=50)
B1.turninit = TurnInit(attack=CombatCode.battledata.DeclareAttack('A1', pglobals.Moves("tackle")))

battle = True

while battle:
    turnorder = calculateTurnorder(testbattle)
    for att in turnorder:
        curpoke = testbattle.positions[att]
        result = pglobals.Result()
        if curpoke.turninit.attack is not None:
            result = damage_calc(curpoke.pokemon, testbattle.positions[curpoke.turninit.attack.target].pokemon, curpoke.turninit.attack.move)
            print(result.text)
            print(result.debug["hp_percent"])

        if len(result.fainted) > 0:
            battle = False
            break



