import CombatCode.battledata
import CombatCode.pokeglobals as pglobals
from CombatCode.battledata import TurnInit
from CombatCode.combatloop import combatloop

team1 = CombatCode.battledata.Team("Player1",
                        [CombatCode.battledata.Pokemon(1, "A", 1, "pikachu", level=50)])
team2 = CombatCode.battledata.Team("Player2",
                        [CombatCode.battledata.Pokemon(1, "B", 1, "hitmonchan", level=50)])

testbattle = CombatCode.battledata.BattleData(team1, team2)
testbattle.turndata.positions["A1"].declareAttack("B1", "tackle")
testbattle.turndata.positions["B1"].declareAttack("A1", "tackle")

combatloop(testbattle.turndata)
