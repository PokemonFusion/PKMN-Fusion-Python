import CombatCode.battledata
import CombatCode.pokeglobals as pglobals
from CombatCode.battledata import TurnInit
from CombatCode.combatloop import combatloop

team1 = CombatCode.battledata.Team("Player1",
                        [CombatCode.battledata.Pokemon(1, "A", 1, "pikachu", level=50)])
team2 = CombatCode.battledata.Team("Player2",
                        [CombatCode.battledata.Pokemon(1, "B", 1, "hitmonchan", level=50)])

testbattle = CombatCode.battledata.BattleData(team1, team2)

testbattle.turndata.positions["A1"] = CombatCode.battledata.PositionData()
A1 = testbattle.turndata.positions["A1"]
A1.pokemon = CombatCode.battledata.Pokemon(1, "A", 1, "pikachu", level=50)

A1.turninit = TurnInit(A1.pokemon.getPosition(),
                       attack=CombatCode.battledata.DeclareAttack('B1', pglobals.Moves("tackle")))
testbattle.turndata.positions["B1"] = CombatCode.battledata.PositionData()
B1 = testbattle.turndata.positions["B1"]
B1.pokemon = CombatCode.battledata.Pokemon(1, "B", 1, "hitmonchan", level=50)
B1.turninit = TurnInit(B1.pokemon.getPosition(),
                       attack=CombatCode.battledata.DeclareAttack('A1', pglobals.Moves("tackle")))

combatloop(testbattle.turndata)
