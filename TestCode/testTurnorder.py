import CombatCode.pokeglobals as pglobals
from CombatCode.battledata import TurnInit
import CombatCode.battledata
from CombatCode.turnorder import calculateTurnorder

testbattle = CombatCode.battledata.TurnData()
testbattle.positions = dict()
testbattle.positions["A1"] = CombatCode.battledata.TurnData()
A1 = testbattle.positions["A1"]
A1.pokemon = CombatCode.battledata.Pokemon(1,"A",1,"pikachu", level=50)

A1.turninit = TurnInit(attack=CombatCode.battledata.DeclareAttack('B1', pglobals.Moves("tackle")))
testbattle.positions["B1"] = CombatCode.battledata.TurnData()
B1 = testbattle.positions["B1"]
B1.pokemon = CombatCode.battledata.Pokemon(1,"B",1,"pikachu",level=50)
B1.turninit = TurnInit(attack=CombatCode.battledata.DeclareAttack('A1', pglobals.Moves("tackle")))

turnorder = calculateTurnorder(testbattle)

print(turnorder)

