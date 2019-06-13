import random
from CombatCode.battledata import TurnInit


"""Assumptions: receiving a battle-round object consisting of the positions involved and what they are doing."""


def calculateTurnorder(battleround) -> list:
    class Priority:
        priorities = list()

        def __init__(self, turndata: TurnInit, pokemon):
            # clear off the temporary variable
            pokemon.tempvals.clear()
            self.priority = 0
            self.speed = 0

            if turndata.switch is not None:
                self.priority = 6
            elif turndata.run is not None:
                self.priority = 9
            elif turndata.item is not None:
                self.priority = 8    
            elif turndata.recharge is not None:
                self.priority = 6
            else:
                self.priority = turndata.attack.move.priority

            self.priorities.append(self.priority)

            self.speed = pokemon.getStat("spd")

            # add random decimal to speed to handle ties
            self.speed += random.uniform(0.0, 0.1)

        @classmethod
        def max(cls) -> int:
            return max(cls.priorities)

        @classmethod
        def min(cls) -> int:
            return min(cls.priorities)

    priorities = {}
    for key, pos in battleround.positions.items():
        priorities[key] = Priority(pos.turninit, pos.pokemon)
    
    # Check for pursuit here  -- TODO: Worry about this later
    # for pos in battleround.positions:
    #     if pos.turninit.attack is not None:
    #         if pos.turninit.attack.move == ''
    
    turnorder = []
    # This may be more complicated than it needs to be, but it will be accurate.

    for pri in range(Priority.max(), Priority.min() - 1, -1):
        if len(turnorder) == len(priorities):
            break
        curpri = []
        for pos, data in priorities.items():
            if data.priority == pri:
                curpri.append(pos)

        if len(curpri) == 0:
            continue
        curpri.sort(key=lambda x: priorities[x].speed, reverse=True)
        turnorder.extend(curpri)

    return turnorder


