import CombatCode.battledata
import CombatCode.pokeglobals as pglobals
from CombatCode.battledata import TurnInit
from CombatCode.combatloop import combatloop

team1 = CombatCode.battledata.Team("Player1",
                        [CombatCode.battledata.Pokemon(1, "pikachu", level=50),
                         CombatCode.battledata.Pokemon(1, "mewtwo", level=50)])
team2 = CombatCode.battledata.Team("Player2",
                        [CombatCode.battledata.Pokemon(1, "hitmonchan", level=50),
                         CombatCode.battledata.Pokemon(1, "charmander", level=50)])

testbattle = CombatCode.battledata.BattleData(team1, team2)
testbattle.turndata.positions["A1"].declareAttack("B1", "tackle")
testbattle.turndata.positions["B1"].declareAttack("A1", "tackle")

faint = []
print(testbattle.validtoswitch('A'))
testbattle.turndata.positions["A1"].declareSwitch(2)
faint = combatloop(testbattle)
testbattle.turndata.positions["A1"].declareAttack("B1", "tackle")

while len(faint) < 1:
    faint = combatloop(testbattle)

print(faint)
for x in faint:
    switchables = testbattle.validtoswitch(x[0])
    print(switchables)
    print(testbattle.faintswitch(x, switchables[0]))


