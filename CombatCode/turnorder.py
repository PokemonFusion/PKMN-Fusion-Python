from CombatCode.battledata import TurnInit

"""Assumptions: recieving a battleround object consisting of the positions involved and what they are doing."""


def calculateTurnorder(battleround) -> list:
    class Priority:
        def __init__(self, turndata: TurnInit, pokemon):
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
                self.speed = pokemon.calculateSpeed()
            
            


    priorities = {}
    for pos in battleround.positions:
        priorities[pos.position] = Priority(pos.turninit, pos.pokemon)
    
    #Check for pursuit here  -- Worry about this later
    # for pos in battleround.positions:
    #     if pos.turninit.attack is not None:
    #         if pos.turninit.attack.move == ''
    
    turnorder = []
    


